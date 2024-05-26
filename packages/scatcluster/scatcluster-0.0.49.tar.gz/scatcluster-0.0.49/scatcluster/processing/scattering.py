import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import obspy
import pandas as pd
import scipy as sp
from matplotlib import dates as mdates
from obspy.clients.filesystem.sds import Client
from obspy.core import UTCDateTime
from obspy.core.stream import Stream
from obspy.core.trace import Trace
from scatseisnet.network import ScatteringNetwork
from scatseisnet.operation import segmentize

from scatcluster.helper import is_gpu_available


class Scattering:

    def reduce_type(self):
        """
        Pooling operation performed on the last axis.
        """
        pooling_options = [
            ('avg', np.mean),
            ('max', np.max),
            ('median', np.median),
            ('std', np.std),
            ('gmean', sp.stats.gmean),
            ('hmean', sp.stats.hmean),
            ('pmean', sp.stats.pmean),
            ('kurtosis', sp.stats.kurtosis),
            ('skew', sp.stats.skew),
            ('entropy', sp.stats.entropy),
            ('sem', sp.stats.sem),
            ('differential_entropy', sp.stats.differential_entropy),
            ('median_abs_deviation', sp.stats.median_abs_deviation),
        ]
        for po in pooling_options:
            if self.network_pooling == po[0]:
                return po[1]

    def load_data_times(self):
        """
        Load the data times from a file and store them in the `data_times` attribute.

        This function reads the data times from a file located at
        `{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_`
        `{self.network_name}_times.npy` and stores them in the `data_times` attribute.

        """
        self.data_times = np.load(
            f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_'
            f'{self.network_name}_times.npy')

    def build_day_list(self) -> None:
        """Build data_day_list object
        """
        day_list = [
            day_start for day_start in pd.date_range(
                UTCDateTime(self.data_starttime).strftime('%Y%m%d'), (UTCDateTime(self.data_endtime) -
                                                                      (60 * 60 * 24)).strftime('%Y%m%d')).format(
                                                                          formatter=lambda x: x.strftime('%Y-%m-%d'))
            if day_start not in [UTCDateTime(day_exc).strftime('%Y-%m-%d') for day_exc in self.data_exclude_days]
        ]

        self.data_day_list = day_list

    def trace_process(self, trace: Trace) -> Trace:
        """Processing happening to all traces

        Args:
            trace (Trace): Obspy trace original

        Returns:
            Trace: process obspy trace
        """
        trace.decimate(2)
        trace.detrend('linear')
        trace.filter(type='highpass', freq=1)
        trace.detrend('demean')
        trace.taper(0.05)
        return trace

    def load_data(self, starttime: UTCDateTime, endtime: UTCDateTime, channel: str) -> Stream:
        """Load the seismic and trim according to data_starttime and data_endtime

        Args:
            starttime (UTCDateTime): Start datetime of the trim
            endtime (UTCDateTime): End datetime of the trim
            channel (str): Channel selected

        Returns:
            Stream: Processed obspy stream
        """
        try:
            client = Client(self.data_client_path)
            stream = client.get_waveforms(network=self.data_network,
                                          station=self.data_station,
                                          location=self.data_location,
                                          channel=channel,
                                          starttime=starttime,
                                          endtime=endtime)

            traces = [self.trace_process(trace) for trace in stream]
            stream = obspy.core.stream.Stream(traces)
            del traces
            stream.merge(method=1, fill_value=0)
            stream.trim(starttime, endtime, pad=True, fill_value=0)
            return stream
        except Exception as e:
            print(f'>> Skipping {starttime}-{endtime} as there was an error in loading data from SDS Client due to {e}')
            return Stream()

    def network_build_scatcluster(self) -> None:
        """Build scatcluster network, assign to self.net and store as pickle
        """
        self.network_samples_per_segment = int(self.network_segment * self.network_sampling_rate)
        self.network_samples_per_step = int(self.network_step * self.network_sampling_rate)
        self.net = ScatteringNetwork(*self.network_banks,
                                     bins=self.network_samples_per_segment,
                                     sampling_rate=self.network_sampling_rate)

        # SAVE NETWORK IN PICKLE FILE
        with open(
                f'{self.data_savepath}networks/{self.data_network}_{self.data_station}_{self.data_location}_'
                f'{self.network_name}.pickle', 'wb') as handle:
            pickle.dump(self.net, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def plot_network_filter_banks(self) -> None:
        """
        Plot the filter banks
        """
        NROWS = len(self.net.banks)
        # Crete axes
        _, ax = plt.subplots(NROWS, 2, sharey='row', figsize=(10, 8))
        # Loop over network layers
        for bank_enum, bank in enumerate(self.net.banks):
            if is_gpu_available():
                bank.wavelets = bank.wavelets.get()
                bank.spectra = bank.spectra.get()
                # bank.ratios = bank.ratios.get()
                # bank.widths = bank.widths.get()
                # bank.centers = bank.centers.get()
                # bank.times = bank.times.get()
                # bank.frequencies = bank.frequencies.get()

            # Limit view to three times the temporal width of largest wavelet
            width_max_label = -1 * min(2.5 * bank.widths.max(), bank.times.max())

            # Show each wavelet

            iterable = zip(bank.wavelets, bank.spectra, bank.ratios, bank.widths, bank.centers)
            for wavelet, spectrum, ratio, width, center in iterable:

                # Time domain
                ax[bank_enum, 0].plot(bank.times, wavelet.real + ratio, 'C0')
                ax[bank_enum, 0].text(width_max_label, ratio, f'{width*4:.2f}', fontsize='small')

                # Spectral domain
                ax[bank_enum, 1].plot(bank.frequencies, np.log(np.abs(spectrum) + 1) + ratio, 'C0')
                ax[bank_enum, 1].text(0.001, ratio, f'{center:.2f}', fontsize='small')

            # Limit view to three times the temporal width of largest wavelet
            width_max = min(3 * bank.widths.max(), bank.times.max())

            # Labels
            ax[bank_enum, 0].set_ylabel(f'Order {bank_enum+1}\nOctaves (base 2 log)')
            ax[bank_enum, 0].set_xlabel('Time (seconds)')
            ax[bank_enum, 0].set_xlim(-width_max, width_max)
            ax[bank_enum, 1].set_xscale('log')
            ax[bank_enum, 1].set_xlabel('Frequency (Hz)')

            ax[bank_enum, 0].text(width_max_label, 0, 'Temporal Width (s)', fontsize='small')
            ax[bank_enum, 1].text(0.001, 0, 'Centre Freq. (Hz)', fontsize='small')
        plt.suptitle(f'scatcluster parametrization for Segment {self.network_segment}: Step {self.network_step}: Banks '
                     f'{self.network_banks_name}')

        plt.savefig(f'{self.data_savepath}figures/{self.data_network}_{self.data_station}_{self.data_location}_'
                    f'{self.network_name}_filter_banks.png')

    def load_sample_data(self) -> Stream:
        """Load sample
        """
        return self.load_data(starttime=UTCDateTime(self.data_sample_starttime),
                              endtime=UTCDateTime(self.data_sample_endtime),
                              channel=self.data_channel)

    def plot_sample_spectra(self) -> None:
        """Plot the Network filter spectra"""
        frequencies = self.net.banks[0].centers
        timestamps = pd.to_datetime(self.sample_times, unit='D')
        timestamps_scats = pd.to_datetime(self.sample_times_scatterings, unit='D')

        _, ax = plt.subplots(2, len(self.channel_list), sharex=True, sharey='row', figsize=(20, 5))

        for channel_num, _ in enumerate(self.channel_list):
            first_order_scattering_coefficients = self.sample_scattering_coefficients[0][:, channel_num, :].squeeze().T
            first_order_scattering_coefficients = np.real(np.log10(first_order_scattering_coefficients))

            ax[0, channel_num].plot(timestamps, self.sample_data[channel_num], rasterized=True)
            ax[0, channel_num].set_title(self.channel_list[channel_num])

            ax[1, channel_num].pcolormesh(timestamps_scats,
                                          frequencies,
                                          first_order_scattering_coefficients,
                                          rasterized=True)
            ax[1, channel_num].set_yscale('log')
            ax[1, channel_num].tick_params('x', labelrotation=90)

        ax[0, 0].set_ylabel('Sample Trace')
        ax[1, 0].set_ylabel('First Order Scat. Coefficients\nFrequency (Hz)')
        plt.subplots_adjust(wspace=0, hspace=0)

        plt.suptitle('Sample Trace ScatCluster Transform')
        plt.savefig(f'{self.data_savepath}figures/{self.data_network}_{self.data_station}_{self.data_location}_'
                    f'{self.network_name}_sample_transform.png')
        plt.show()

    def process_sample_data(self) -> None:
        """Process the sample data range. This involes:
        (1) load the data and process,
        (2) define the sample_times and sample_data,
        (3) segmentize into sample_data_segments and respective sample_times_scatterings,
        (4) transform into sample_scattering_coefficients,
        (5) plot filter spectra
        """
        self.sample_stream = self.load_sample_data()
        self.sample_times = self.sample_stream[0].times('matplotlib')
        self.sample_data = np.array([trace.data for trace in self.sample_stream])
        self.channel_list = [trace.stats.channel for trace in self.sample_stream]

        self.sample_data_segments = segmentize(self.sample_data, self.network_samples_per_segment,
                                               self.network_samples_per_step)
        self.sample_times_scatterings = segmentize(self.sample_times, self.network_samples_per_segment,
                                                   self.network_samples_per_step)[:, 0]
        self.sample_scattering_coefficients = self.net.transform(self.sample_data_segments, self.reduce_type())
        self.plot_sample_spectra()

    def plot_seismic(self, sample: bool = False):
        """
        Plot the seismic data.

        Parameters:
            sample (bool): If True, plot the sample data. Otherwise, plot the regular data.

        """
        if sample:
            if self.sample_data is None:
                self.sample_stream = self.load_sample_data()
                self.sample_times = self.sample_stream[0].times('matplotlib')
                self.sample_data = np.array([trace.data for trace in self.sample_stream])
                self.channel_list = [trace.stats.channel for trace in self.sample_stream]

            times = self.sample_times
            data = self.sample_data
            channel_list = self.channel_list
        else:
            if self.data_all is None:
                self.data_stream = self.load_data(starttime=UTCDateTime(self.data_starttime),
                                                  endtime=UTCDateTime(self.data_endtime),
                                                  channel=self.data_channel)
                self.data_times = self.data_stream[0].times('matplotlib')
                self.data_all = np.array([trace.data for trace in self.data_stream])
                self.channel_list = [trace.stats.channel for trace in self.data_stream]
            times = self.data_times
            data = self.data_all
            channel_list = self.channel_list

        # Plot
        _, axes = plt.subplots(3, 1, figsize=(20, 10), sharex=True, sharey=True)
        for channel_enum, channel in enumerate(channel_list):
            axes[channel_enum].plot(times, data[channel_enum, :])
            axes[channel_enum].set_ylabel(f'{channel}')

        dateticks = mdates.AutoDateLocator()
        datelabels = mdates.ConciseDateFormatter(dateticks)
        axes[0].xaxis.set_major_locator(dateticks)
        axes[0].xaxis.set_major_formatter(datelabels)
        axes[0].set_xlim(times.min(), times.max())

    def process_scatcluster_yyyy_mm_dd(self, day_start: str, day_end: str) -> None:
        """Process scatcluster for a single day.

        Args:
            day_start (str): Start day of format "YYYY-MM-DD"
            day_end (str): End day of format "YYYY-MM-DD"
        """
        print(f'Processing {day_start} - {day_end}')
        scatterings_path = (f'{self.data_savepath}scatterings/{self.data_network}_{self.data_station}_'
                            f'{self.data_location}_{self.network_name}_scatterings_{day_start}.npz')
        if os.path.exists(scatterings_path):
            print('> Scatterings already exist')
        else:
            # Check if day_start exits is valid in data_day_start
            if day_start not in self.data_day_list:
                print(f'> Processing of {day_start} has been excluded as it is part of `data_exclude_days` parameter.')
            else:
                stream = self.load_data(starttime=UTCDateTime(day_start),
                                        endtime=UTCDateTime(day_end),
                                        channel=self.data_channel)
                if len(stream.traces) == 0:
                    print(f'>> Skipping {day_start} as there is no traces')
                elif len(stream.traces) < 3:
                    print(f'>> Skipping {day_start} as there is not all 3 channels')
                else:
                    # Numpyification
                    times = stream[0].times('matplotlib')
                    data = np.array([trace.data for trace in stream])

                    # Segmentization
                    data_segments = segmentize(data, self.network_samples_per_segment, self.network_samples_per_step)
                    times_scat = segmentize(times, self.network_samples_per_segment, self.network_samples_per_step)[:,
                                                                                                                    0]

                    # Scattering transform
                    scattering_coefficients = self.net.transform(data_segments, self.reduce_type())

                    # SAVE SCATTERING COEFFICIENTS IN NPZ FILE
                    np.savez(scatterings_path,
                             scat_coef_0=scattering_coefficients[0],
                             scat_coef_1=scattering_coefficients[1],
                             times=times_scat)

    def process_scatcluster_for_range(self) -> None:
        """Process scatcluster_yyyy_mm_dd for range of YYYY-MM-DDs
        """
        self.build_day_list()
        if len(self.data_day_list) > 0:
            print(f'The following days will be excluded from the analysis: {self.data_exclude_days}')

        for day_start, day_end in zip(
                pd.date_range(
                    UTCDateTime(self.data_starttime).strftime('%Y%m%d'),
                    (UTCDateTime(self.data_endtime) -
                     (60 * 60 * 24)).strftime('%Y%m%d')).format(formatter=lambda x: x.strftime('%Y-%m-%d')),
                pd.date_range(
                    (UTCDateTime(self.data_starttime) + (60 * 60 * 24)).strftime('%Y%m%d'),
                    UTCDateTime(
                        self.data_endtime).strftime('%Y%m%d')).format(formatter=lambda x: x.strftime('%Y-%m-%d'))):
            self.process_scatcluster_yyyy_mm_dd(day_start, day_end)

    def process_vectorized_scattering_coefficients(self) -> None:
        """
        Process the vectorized scattering coefficients by loading data from files, reshaping the coefficients,
        standardizing in log space, and vectorizing them. Display statistics from the vectorization and store the
        processed data.

        Parameters:
            self: An instance of the class.
        """
        file_list = [(f'{self.data_savepath}scatterings/{self.data_network}_{self.data_station}_{self.data_location}_'
                      f'{self.network_name}_scatterings_{day_start}.npz') for day_start in self.data_day_list]

        # LOAD DATA
        TIMES = []
        SC0 = []
        SC1 = []
        for file in file_list:
            try:
                scat_file = np.load(file)
                TIMES.append(scat_file['times'])
                SC0.append(scat_file['scat_coef_0'])
                SC1.append(scat_file['scat_coef_1'])
            except FileNotFoundError:
                print(f'{file} is missing. This has been skipped.')
        times = np.hstack(TIMES)
        del TIMES
        scat_coef_0 = np.vstack(SC0)
        del SC0
        scat_coef_1 = np.vstack(SC1)
        del SC1

        # RESHAPE THE SCATTERING COEFFICIENTS, STANDARDIZE IN LOG SPACE AND VECTORIZE THEM
        scat_coef_0_reshaped = scat_coef_0.reshape(scat_coef_0.shape[0], scat_coef_0.shape[1] * scat_coef_0.shape[2])
        scat_coef_1_reshaped = (scat_coef_1.reshape(scat_coef_1.shape[0],
                                                    scat_coef_1.shape[1] * scat_coef_1.shape[2] * scat_coef_1.shape[3]))

        # # Mask values for which f1 is smaller than f2
        # coefficients.order_2.data = coefficients.order_2.where(
        #     coefficients.f1 >= coefficients.f2, np.nan
        # )

        # # Remove NaNs
        # coefficients = coefficients.dropna(dim="time", how="all")

        # # Normalize
        # dims = ["time", "f1", "f2"]
        # coefficients.order_1.data -= coefficients.order_1.mean(dim=["time", "f1", "channel"]).data
        # coefficients.order_1.data /= coefficients.order_1.std(dim=["time", "f1", "channel"]).data
        # coefficients.order_2.data -= coefficients.order_2.mean(dim=["time", "f1", "f2", "channel"]).data
        # coefficients.order_2.data /= coefficients.order_2.std(dim=["time", "f1", "f2", "channel"]).data

        scat_coef_vectorized = np.hstack((scat_coef_0_reshaped, scat_coef_1_reshaped))
        # Store as part of self
        self.data_times = times
        self.data_scat_coef_vectorized = np.abs(np.log10(scat_coef_vectorized + 0.00001))

        # Display statistics from the vectorization
        print(f'Number of time windows of size {self.network_segment}s: {int(self.data_times.shape[0])}')
        print(f'Number of days investigated: {int((self.network_segment * self.data_times.shape[0])/86400)}')
        print(f'Number of Scat Coefficients: {int(self.data_scat_coef_vectorized.shape[1])}')
        print(f'Vectorized Scat Coefficients: {self.data_scat_coef_vectorized.shape}')

        # Store Data
        np.save(
            f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_'
            f'{self.network_name}_times.npy', self.data_times)
        np.save(
            f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_'
            f'{self.network_name}_scat_coef_vectorized.npy', self.data_scat_coef_vectorized)

    def preload_times(self):
        """
        Preloads the times data from a numpy file and assigns it to the `data_times` attribute of the class.

        """
        data_times = np.load(f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_'
                             f'{self.network_name}_times.npy')
        self.data_times = data_times

    def load_scat_coef_vectorized(self):
        if not hasattr(self, 'scat_coef_vectorized'):
            self.scat_coef_vectorized = np.load(
                f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_'
                f'{self.network_name}_scat_coef_vectorized.npy')
        else:
            print('SC.scat_coef_vectorized already exist')

        return self.scat_coef_vectorized

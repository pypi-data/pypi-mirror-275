from __future__ import annotations

import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Any, Dict, Literal, Mapping, Optional, Protocol, Sequence, Union

import requests
from typing_extensions import TypeAlias

from chalk._gen.chalk.auth.v1.permissions_pb2 import Permission
from chalk.client.exc import ChalkAuthException, ChalkBaseException
from chalk.client.models import (
    BranchDeployResponse,
    BranchIdParam,
    BulkOnlineQueryResponse,
    ChalkError,
    ChalkException,
    DatasetFilter,
    ErrorCode,
    ErrorCodeCategory,
    FeatureDropResponse,
    FeatureObservationDeletionResponse,
    FeatureReference,
    FeatureResult,
    GetIncrementalProgressResponse,
    OfflineQueryContext,
    OnlineQuery,
    OnlineQueryContext,
    OnlineQueryResponse,
    PlanQueryResponse,
    QueryMeta,
    QueryStatus,
    ResolverRunResponse,
    StreamResolverTestResponse,
    WhoAmIResponse,
)
from chalk.features import DataFrame, Feature
from chalk.features._encoding.json import FeatureEncodingOptions
from chalk.features.resolver import Resolver, ResolverProtocol
from chalk.features.tag import BranchId, DeploymentId, EnvironmentId
from chalk.parsed.branch_state import BranchGraphSummary

if TYPE_CHECKING:
    import pandas as pd
    import polars as pl


class DatasetRevision(Protocol):
    """Class wrapper around revisions for Datasets."""

    revision_id: uuid.UUID
    """UUID for the revision job."""

    creator_id: str
    """UUID for the creator of the job."""

    outputs: list[str]
    """Output features for the dataset revision."""

    givens_uri: str | None
    """Location of the givens stored for the dataset."""

    status: QueryStatus
    """Status of the revision job."""

    filters: DatasetFilter
    """Filters performed on the dataset."""

    num_partitions: int
    """Number of partitions for revision job."""

    output_uris: str
    """Location of the outputs stored fo the dataset."""

    output_version: int
    """Storage version of the outputs."""

    num_bytes: int | None = None
    """Number of bytes of the output, updated upon success."""

    created_at: datetime | None = None
    """Timestamp for creation of revision job."""

    started_at: datetime | None = None
    """Timestamp for start of revision job."""

    terminated_at: datetime | None = None
    """Timestamp for end of revision job."""

    dataset_name: str | None = None
    """Name of revision, if given."""

    dataset_id: uuid.UUID | None = None
    """ID of revision, if name is given."""

    dashboard_url: str | None = None
    """url linking to relevant dashboard page"""

    environment: str

    num_computers: int
    """Number of computers this query ran on."""

    branch: str | None = None
    """Name of branch"""

    errors: list[ChalkError] | None = None

    @property
    def url(self) -> str | None:
        """url linking to relevant dashboard page"""
        return self.dashboard_url

    def to_polars(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.DataFrame:
        """Loads a `pl.DataFrame` containing the output. Use `.to_polars_lazyframe()` if you want
        a `LazyFrame` instead, which allows local filtering of datasets that are larger than memory.

        Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pl.LazyFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        Returns
        -------
        pl.DataFrame
            A `pl.DataFrame` materializing query output data.
        """
        ...

    def to_polars_lazyframe(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the output. This method is appropriate for working with larger-than-memory datasets.
        Use `.to_polars()` if you want a `DataFrame` instead.

        Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pl.LazyFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query output data.
        """
        ...

    def get_data_as_polars(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the output.

        Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pl.LazyFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query output data.
        """
        ...

    def get_data_as_pandas(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pd.DataFrame:
        """Loads a `pd.DataFrame` containing the output.

        Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pd.DataFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pd.DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pd.DataFrame
            A `pd.DataFrame` materializing query output data.
        """
        ...

    def get_data_as_dataframe(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> DataFrame:
        """Loads a Chalk `DataFrame` containing the output.


        Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data\
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        DataFrame
            A `DataFrame` materializing query output data.
        """
        ...

    def download_uris(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> Sequence[str]:
        """
        Returns a list of the output uris for the revision. Data
        will be stored in .parquet format. The URIs should be considered temporary,
        and will expire after a server-defined time period.
        """
        ...

    def wait(
        self,
        timeout: float | timedelta | ellipsis | None = ...,
        show_progress: bool = True,
    ) -> None:
        """
        Waits for an offline query job to complete.
        Raises if the query is unsuccessful, otherwise returns itself on success.

        Parameters
        ----------
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        show_progress
            Whether to show a progress bar
        """
        ...

    def download_data(
        self,
        path: str,
        output_id: bool = False,
        output_ts: Union[bool, str] = False,
        ignore_errors: bool = False,
        executor: ThreadPoolExecutor | None = None,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> None:
        """Downloads output files pertaining to the revision to given path.

        Datasets are stored in Chalk as sharded Parquet files. With this
        method, you can download those raw files into a directory for processing
        with other tools.

        Parameters
        ----------
        path
            A directory where the Parquet files from the dataset will be downloaded.
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        executor:
            The executor to use for parallelizing downloads. If None, the default executor will be used.
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        """
        ...

    def get_input_dataframe(
        self,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the inputs.

        Parameters
        ----------
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query input data.
        """
        ...

    def open_in_browser(self, return_url_only: bool = False) -> str:
        """returns and opens a url that opens the offline query page in the Chalk dashboard. Must be logged in.

        Parameters
        ------
        return_url_only
            If True, does not open url in browser. Default is False.

        Returns
        -------
        str
            A url redirecting to the Chalk dashboard.
        """
        ...

    def wait_for_completion(
        self,
        show_progress: bool = True,
        timeout: float | timedelta | ellipsis | None = ...,
    ) -> None:
        """Waits for the revision job to complete.

        `ChalkClient.offline_query` returns a `DatasetRevision` instance immediately after
        submitting the revision job. This method can be used to wait for the
        revision job to complete.

        Once the revision job is complete, the `status` attribute of the
        `DatasetRevision` instance will be updated to reflect the status of the
        revision job.

        If the revision job was successful, you can then use methods such as
        `get_data_as_pandas()` without having to wait for the revision job to
        complete.

        Parameters
        ----------
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        """
        ...

    def ingest(self, store_online: bool = False, store_offline: bool = True) -> Dataset:
        """
        Saves this revision to Chalk's online and offline storage.

        Parameters
        ----------
        store_online
            Whether to store the revision in Chalk's online storage.
        store_offline
            Whether to store the revision in Chalk's offline storage.
        """
        ...

    def resolver_replay(
        self,
        resolver: ResolverProtocol,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> Union[pl.DataFrame, pl.LazyFrame, Mapping[str, pl.DataFrame], Mapping[str, pl.LazyFrame],]:
        """
        Downloads the resolver replay data for the given resolver in the revision, provided the revision had store_plan_stages
        enabled.

        The replay data is functionally similar to viewing the intermediate results on the plan explorer.

        If the resolver appears in only one stage of the plan, the resolver's replay data is returned directly.
        If the resolver instead appears in multiple stages of the plan, a mapping of the operation's ID to the replay data
        will be returned. If the resolver does not appear in the plan, an exception will be thrown.

        Parameters
        ----------
        resolver
            The resolver to download the replay data for, or its fqn.
        show_progress
            Whether to show a progress bar
        lazy
            Whether to return Polars LazyFrames
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        """
        ...


class Dataset(Protocol):
    """Wrapper around Offline Query results.

    Datasets are obtained by invoking `ChalkClient.offline_query()`.
    `Dataset` instances store important metadata and enable the retrieval of
    offline query outputs.

    Examples
    --------
    >>> from chalk.client import ChalkClient, Dataset
    >>> uids = [1, 2, 3, 4]
    >>> at = datetime.now()
    >>> dataset: Dataset = ChalkClient().offline_query(
    ...     input={
    ...         User.id: uids,
    ...         User.ts: [at] * len(uids),
    ...     },
    ...     output=[
    ...         User.id,
    ...         User.fullname,
    ...         User.email,
    ...         User.name_email_match_score,
    ...     ],
    ...     dataset_name='my_dataset'
    ... )
    >>> df = dataset.get_data_as_pandas()
    >>> df.recompute(features=[User.fraud_score], branch="feature/testing")
    """

    is_finished: bool
    """Whether the most recent `DatasetRevision` is finished or still pending."""

    version: int
    """Storage version number of outputs."""

    revisions: Sequence[DatasetRevision]
    """A list of all `DatasetRevision` instances belonging to this dataset."""

    dataset_name: str | None
    """The unique name for this dataset, if given."""

    dataset_id: uuid.UUID | None
    """The unique UUID for this dataset."""

    errors: Sequence[ChalkError] | None
    """A list of errors in loading the dataset, if they exist."""

    def to_polars(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.DataFrame:
        """Loads a `pl.DataFrame` containing the output. Use `.to_polars_lazyframe()` if you want
        a `LazyFrame` instead, which allows local filtering of datasets that are larger than memory.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pl.LazyFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        Returns
        -------
        pl.DataFrame
            A `pl.DataFrame` materializing query output data.
        """
        ...

    def to_polars_lazyframe(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the output. This method is appropriate for working with larger-than-memory datasets.
        Use `.to_polars()` if you want a `DataFrame` instead.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pl.LazyFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query output data.
        """
        ...

    def get_data_as_polars(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the output.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pl.LazyFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query output data.
        """
        ...

    def get_data_as_pandas(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pd.DataFrame:
        """Loads a `pd.DataFrame` containing the output.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pd.DataFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pd.DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pd.DataFrame
            A `pd.DataFrame` materializing query output data.
        """
        ...

    def get_data_as_dataframe(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> DataFrame:
        """Loads a Chalk `DataFrame` containing the output.
        Requires the pertinent Chalk features to be accessible via import

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        DataFrame
            A `DataFrame` materializing query output data.
        """
        ...

    def to_pandas(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pd.DataFrame:
        """Loads a `pd.DataFrame` containing the output of the most recent revision.

        Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pd.DataFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pd.DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pd.DataFrame
            A `pd.DataFrame` materializing query output data.
        """
        ...

    def download_uris(
        self,
        output_id: bool = False,
        output_ts: bool | str = False,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> list[str]:
        """
        Returns a list of the output uris for the revision. Data
        will be stored in .parquet format. The URIs should be considered temporary,
        and will expire after a server-defined time period.

        Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pd.DataFrame`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `pd.DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        ignore_errors
            Whether to ignore query errors upon fetching data
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        """
        ...

    def wait(
        self,
        timeout: float | timedelta | ellipsis | None = ...,
        show_progress: bool = True,
    ) -> Dataset:
        """
        Waits for an offline query job to complete. Returns a list of errors if unsuccessful, or None if successful.

        Parameters
        ----------
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        show_progress
            Whether to show a progress bar
        """
        ...

    def download_data(
        self,
        path: str,
        executor: ThreadPoolExecutor | None = None,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> None:
        """Downloads output files pertaining to the revision to the given path.

        Datasets are stored in Chalk as sharded Parquet files. With this
        method, you can download those raw files into a directory for processing
        with other tools.

        Parameters
        ----------
        path
            A directory where the Parquet files from the dataset will be downloaded.
        ignore_errors
            Whether to ignore query errors upon fetching data
        executor
            An executor to use to download the data in parallel. If not specified, the default executor will be used.
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        Examples
        ----------
        >>> from chalk.client import ChalkClient, Dataset
        >>> uids = [1, 2, 3, 4]
        >>> at = datetime.now()
        >>> dataset: Dataset = ChalkClient().offline_query(
        ...     input={
        ...         User.id: uids,
        ...         User.ts: [at] * len(uids),
        ...     },
        ...     output=[
        ...         User.id,
        ...         User.fullname,
        ...         User.email,
        ...         User.name_email_match_score,
        ...     ],
        ...     dataset_name='my_dataset'
        ... )
        >>> dataset.download_data('my_directory')
        """
        ...

    def get_input_dataframe(
        self,
        ignore_errors: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the inputs that were used to create the dataset.

        Parameters
        ----------
        ignore_errors
            Whether to ignore query errors upon fetching data
        executor
            An executor to use to download the data in parallel. If not specified, the default executor will be used.
        show_progress
            Whether to show a progress bar
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query input data.
        """
        ...

    def open_in_browser(self, return_url_only: bool = False) -> str:
        """returns and opens a url that opens the offline query page in the Chalk dashboard. Must be logged in.

        Parameters
        ------
        return_url_only
            If True, does not open url in browser. Default is False.

        Returns
        -------
        str
            A url redirecting to the Chalk dashboard.
        """
        ...

    def recompute(
        self,
        features: list[FeatureReference] | None = None,
        branch: str | None = None,
        wait: bool = True,
        show_progress: bool = False,
        store_plan_stages: bool = False,
        correlation_id: str | None = None,
        explain: bool | Literal["only"] = False,
        tags: list[str] | None = None,
        required_resolver_tags: list[str] | None = None,
        planner_options: Mapping[str, Union[str, int, bool]] | None = None,
        use_multiple_computers: bool = False,
        timeout: float | timedelta | None | ellipsis = ...,
    ) -> Dataset:
        """Creates a new revision of this `Dataset` by recomputing the specified features.

        Carries out the new computation on the branch specified when constructing the client.

        Parameters
        ------
        features
            A list of specific features to recompute. Features that don't exist in the dataset will be added.
            Features that already exist in the dataset will be recomputed.
            If not provided, all the existing features in the dataset will be recomputed.
        branch
            If specified, Chalk will route your request to the relevant branch.
            If None, Chalk will route your request to a non-branch deployment.
            If not specified, Chalk will use the current client's branch info.
        show_progress
            If True, progress bars will be shown while recomputation is running.
            This flag will also be propogated to the methods of the resulting
            `Dataset`.
        correlation_id
            You can specify a correlation ID to be used in logs and web interfaces.
            This should be globally unique, i.e. a `uuid` or similar. Logs generated
            during the execution of your query will be tagged with this correlation id.
        store_plan_stages
            If True, the output of each of the query plan stages will be stored
            in S3/GCS. This will dramatically impact the performance of the query,
            so it should only be used for debugging.
            These files will be visible in the web dashboard's query detail view, and
            can be downloaded in full by clicking on a plan node in the query plan visualizer.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        required_resolver_tags
            If specified, *all* required_resolver_tags must be present on a resolver for it to be
            considered eligible to execute.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.

        Raises
        ------
        ValueError
            If no branch was provided to the Chalk Client.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> dataset = ChalkClient(branch="data_science").offline_query(...)
        >>> df = dataset.get_data_as_polars()
        >>> # make changes to resolvers in your project
        >>> dataset.recompute()
        >>> new_df = dataset.get_data_as_polars() # receive newly computed data
        """
        ...

    def ingest(self, store_online: bool = False, store_offline: bool = True) -> Dataset:
        """
        Saves the latest revision of this dataset to Chalk's online and offline storage.

        Parameters
        ----------
        store_online
            Whether to store the revision in Chalk's online storage.
        store_offline
            Whether to store the revision in Chalk's offline storage.
        """
        ...

    def resolver_replay(
        self,
        resolver: ResolverProtocol,
        show_progress: bool = True,
        timeout: float | timedelta | ellipsis | None = ...,
    ) -> Union[pl.DataFrame, pl.LazyFrame, Mapping[str, pl.DataFrame], Mapping[str, pl.LazyFrame],]:
        """
        Downloads the resolver replay data for the given resolver in the latest revision of the dataset.

        The replay data is functionally similar to viewing the intermediate results on the plan explorer.

        If the resolver appears in only one stage of the plan, the resolver's replay data is returned directly.
        If the resolver instead appears in multiple stages of the plan, a mapping of the operation's ID to the replay data
        will be returned. If the resolver does not appear in the plan, an exception will be thrown.

        Parameters
        ----------
        resolver
            The resolver to download the replay data for, or its fqn.
        lazy:
            Whether to return Polars LazyFrames or DataFrames
        show_progress
            Whether to show progress bars
        timeout
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        """
        ...


class BulkQueryResponse(Protocol):
    scalars_df: pl.DataFrame | None
    groups_dfs: Dict[str, pl.DataFrame] | None
    errors: list[ChalkError] | None
    meta: QueryMeta | None

    def get_feature_value(self, feature: FeatureReference) -> Any:
        """Convenience method for accessing feature values from the data response

        Parameters
        ----------
        feature
            The feature or its string representation.

        Returns
        -------
        Any
            The value of the feature.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> data = ChalkClient().query(...)
        >>> data.get_feature_value(User.name)
        "Katherine Johnson"
        >>> data.get_feature_value("user.name")
        "Katherine Johnson"
        """
        ...


class QueryBulkResponse(Protocol):
    responses: list[BulkQueryResponse]


class OnlineQueryResult(Protocol):
    data: list[FeatureResult]
    """The output features and any query metadata."""

    errors: list[ChalkError] | None
    """Errors encountered while running the resolvers.

    If no errors were encountered, this field is empty.
    """

    meta: QueryMeta | None
    """Metadata about the query execution.
    Only present if `include_meta=True` is passed to the relevant query method.
    """

    def get_feature(self, feature: FeatureReference) -> FeatureResult | None:
        """Convenience method for accessing feature result from the data response.

        Parameters
        ----------
        feature
            The feature or its string representation.

        Returns
        -------
        FeatureResult | None
            The `FeatureResult` for the feature, if it exists.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> data = ChalkClient().query(...)
        >>> data.get_feature(User.name).ts
        datetime.datetime(2023, 2, 5, 23, 25, 26, 427605)
        >>> data.get_feature("user.name").meta.cache_hit
        False
        """
        ...

    def get_feature_value(self, feature: FeatureReference) -> Any:
        """Convenience method for accessing feature values from the data response.

        Parameters
        ----------
        feature
            The feature or its string representation.

        Returns
        -------
        Any
            The value of the feature.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> data = ChalkClient().query(...)
        >>> data.get_feature_value(User.name)
        "Katherine Johnson"
        >>> data.get_feature_value("user.name")
        "Katherine Johnson"
        """
        ...


class ChalkClient:
    """The `ChalkClient` is the primary Python interface for interacting with Chalk.

    You can use it to query data, trigger resolver runs, gather offline data, and more.
    """

    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        environment: EnvironmentId | None = None,
        api_server: str | None = None,
        branch: BranchId | None = None,
        preview_deployment_id: DeploymentId | None = None,
        session: requests.Session | None = None,
        query_server: str | None = None,
        additional_headers: Mapping[str, str] | None = None,
        default_job_timeout: float | timedelta | None | ellipsis = ...,
    ):
        """Create a `ChalkClient` with the given credentials.

        Parameters
        ----------
        client_id
            The client ID to use to authenticate. Can either be a
            service token id or a user token id.
        client_secret
            The client secret to use to authenticate. Can either be a
            service token secret or a user token secret.
        environment
            The ID or name of the environment to use for this client.
            Not necessary if your `client_id` and `client_secret`
            are for a service token scoped to a single environment.
            If not present, the client will use the environment variable
            `CHALK_ENVIRONMENT`.
        api_server
            The API server to use for this client. Required if you are
            using a Chalk Dedicated deployment. If not present, the client
            will check for the presence of the environment variable
            `CHALK_API_SERVER`, and use that if found.
        query_server
            The query server to use for this client. Required if you are
            using a standalone Chalk query engine deployment. If not present,
            the client will default to the value of api_server.
        branch
            If specified, Chalk will route all requests from this client
            instance to the relevant branch. Some methods allow you to
            override this instance-level branch configuration by passing
            in a `branch` argument.
        preview_deployment_id
            If specified, Chalk will route all requests from this client
            instance to the relevant preview deployment.
        session
            A `requests.Session` to use for all requests. If not provided,
            a new session will be created.
        additional_headers
            A map of additional HTTP headers to pass with each request.
        default_job_timeout:
            The default wait timeout, in seconds, to wait for long-running jobs to complete
            when accessing query results.
            Jobs will not timeout if this timeout elapses. For no timeout, set to None.
            The default timeout is 10 minutes.
        Raises
        ------
        ChalkAuthException
            If `client_id` or `client_secret` are not provided, there
            is no `~/.chalk.yml` file with applicable credentials,
            and the environment variables `CHALK_CLIENT_ID` and
            `CHALK_CLIENT_SECRET` are not set.
        """
        super().__init__()
        ...

    def query(
        self,
        input: Mapping[FeatureReference, Any] | Any,
        output: Sequence[FeatureReference] = (),
        now: datetime | None = None,
        staleness: Mapping[FeatureReference, str] | None = None,
        environment: EnvironmentId | None = None,
        tags: list[str] | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        query_name: str | None = None,
        query_name_version: str | None = None,
        include_meta: bool = False,
        meta: Mapping[str, str] | None = None,
        explain: bool | Literal["only"] = False,
        store_plan_stages: bool = False,
        encoding_options: FeatureEncodingOptions | None = None,
        required_resolver_tags: list[str] | None = None,
        planner_options: Mapping[str, Union[str, int, bool]] | None = None,
        request_timeout: Optional[float] = None,
    ) -> OnlineQueryResult:
        """Compute features values using online resolvers.
        See https://docs.chalk.ai/docs/query-basics for more information.

        Parameters
        ----------
        input
            The features for which there are known values, mapped to those values.
            For example, `{User.id: 1234}`. Features can also be expressed as snakecased strings,
            e.g. `{"user.id": 1234}`
        output
            Outputs are the features that you'd like to compute from the inputs.
            For example, `[User.age, User.name, User.email]`.

            If an empty sequence, the output will be set to all features on the namespace
            of the query. For example, if you pass as input `{"user.id": 1234}`, then the query
            is defined on the `User` namespace, and all features on the `User` namespace
            (excluding has-one and has-many relationships) will be used as outputs.
        staleness
            Maximum staleness overrides for any output features or intermediate features.
            See https://docs.chalk.ai/docs/query-caching for more information.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        required_resolver_tags
            If specified, *all* required_resolver_tags must be present on a resolver for it to be
            considered eligible to execute.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the relevant preview deployment.
        query_name
            The semantic name for the query you're making, for example, `"loan_application_model"`.
            Typically, each query that you make from your application should have a name.
            Chalk will present metrics and dashboard functionality grouped by 'query_name'.
        include_meta
            Returns metadata about the query execution under `OnlineQueryResult.meta`.
            This could make the query slightly slower.
            For more information, see https://docs.chalk.ai/docs/query-basics.
        explain
            Log the query execution plan. Requests using `explain=True` will be slower
            than requests using `explain=False`. If `"only"`, the query will not be executed,
            and only the query plan will be returned.

            If `True`, 'include_meta' will be set to `True` as well.
        store_plan_stages
            If `True`, the output of each of the query plan stages will be stored.
            This option dramatically impacts the performance of the query,
            so it should only be used for debugging.
        correlation_id
            You can specify a correlation ID to be used in logs and web interfaces.
            This should be globally unique, i.e. a `uuid` or similar. Logs generated
            during the execution of your query will be tagged with this correlation id.
        now
            The time at which to evaluate the query. If not specified, the current time will be used.
            This parameter is complex in the context of online_query since the online store
            only stores the most recent value of an entity's features. If `now` is in the past,
            it is extremely likely that `None` will be returned for cache-only features.

            This parameter is primarily provided to support:
                - controlling the time window for aggregations over cached has-many relationships
                - controlling the time wnidow for aggregations over has-many relationships loaded from an
                  external database

            If you are trying to perform an exploratory analysis of past feature values, prefer `offline_query`.

        Other Parameters
        ----------------
        meta
            Arbitrary `key:value` pairs to associate with a query.

        planner_options
            Dictionary of additional options to pass to the Chalk query engine.
            Values may be provided as part of conversations with Chalk support to
            to enable or disable specific functionality.

        request_timeout
            Float value indicating number of seconds that the request should wait before timing out
            at the network level. May not cancel resources on the server processing the query.

        Returns
        -------
        OnlineQueryResult
            Wrapper around the output features and any query metadata,
            plus errors encountered while running the resolvers.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> result = ChalkClient().query(
        ...     input={
        ...         User.name: "Katherine Johnson"
        ...     },
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        >>> result.get_feature_value(User.fico_score)
        """
        ...

    def multi_query(
        self,
        queries: list[OnlineQuery],
        environment: EnvironmentId | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        query_name: str | None = None,
        query_name_version: str | None = None,
        meta: Mapping[str, str] | None = None,
        use_feather: bool | None = True,
        compression: str | None = "uncompressed",
    ) -> BulkOnlineQueryResponse:
        """
        Execute multiple queries (represented by `queries=` argument) in a single request. This is useful if the
        queries are "rooted" in different `@features` classes -- i.e. if you want to load features for `User` and
        `Merchant` and there is no natural relationship object which is related to both of these classes, `multi_query`
        allows you to submit two independent queries.

        Returns a BulkOnlineQueryResponse, which is functionally a list of query results. Each of these result
        can be accessed by index. Individual results can be further checked for errors and converted
        to pandas or polars DataFrames.

        In contrast, `query_bulk` executes a single query with multiple inputs/outputs.

        Parameters
        ----------
        queries
            A list of the OnlineQueries you'd like to execute.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.

        Other Parameters
        ----------------
        query_name
            The name for class of query you're making, for example, `"loan_application_model"`.
        correlation_id
            A globally unique ID for the query, used alongside logs and
            available in web interfaces.
        meta
            Arbitrary `key:value` pairs to associate with a query.
        compression
            Which compression scheme to use pyarrow. Options are: {"zstd", "lz4", "uncompressed"}.

        Returns
        -------
        BulkOnlineQueryResponse
            An output containing results: list[BulkOnlineQueryResult], where each result contains
            dataframes of the results of each query or any errors.

        Examples
        --------
        >>> from chalk.client import ChalkClient, OnlineQuery
        >>> queries =[
        ...     OnlineQuery(input={User.name: ['Katherine Johnson'], output=[User.fico_score]}),
        ...     OnlineQuery(input={Merchant.name': ['Myrrh Chant'], output=['Merchant.address']}),
        ...     OnlineQuery(input={NonFeature.wrong': ['Wrong!'], output=['NonFeature.wrong']}),
        ... ]
        >>> result = ChalkClient().multi_query(
        ...     queries=queries,
        ... )
        >>> result[0].get_feature_value(User.fico_score)
        >>> queries_with_errors = [q for q, r in zip(queries, result) if r.errors is not None]
        """
        ...

    def query_bulk(
        self,
        input: Mapping[FeatureReference, Sequence[Any]],
        output: Sequence[FeatureReference],
        now: Sequence[datetime] | None = None,
        staleness: Mapping[FeatureReference, str] | None = None,
        context: OnlineQueryContext | None = None,  # Deprecated.
        environment: EnvironmentId | None = None,
        tags: list[str] | None = None,
        required_resolver_tags: list[str] | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        query_name: str | None = None,
        query_name_version: str | None = None,
        meta: Mapping[str, str] | None = None,
    ) -> BulkOnlineQueryResponse:
        """Compute features values for many rows of inputs using online resolvers.
        See https://docs.chalk.ai/docs/query-basics for more information on online query.

        This method is similar to `query`, except it takes in `list` of inputs, and produces one
        output per row of inputs.

        This method is appropriate if you want to fetch the same set of features for many different
        input primary keys.

        This method contrasts with `multi_query`, which executes multiple fully independent queries.

        This endpoint is not available in all environments.


        Parameters
        ----------
        input
            The features for which there are known values, mapped to a list
            of the values.
        output
            Outputs are the features that you'd like to compute from the inputs.
        staleness
            Maximum staleness overrides for any output features or intermediate features.
            See https://docs.chalk.ai/docs/query-caching for more information.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.
        now
            The time at which to evaluate the query. If not specified, the current time will be used.
            The length of this list must be the same as the length of the values in `input`.

        Other Parameters
        ----------------
        query_name
            The name for class of query you're making, for example, `"loan_application_model"`.
        correlation_id
            A globally unique ID for the query, used alongside logs and
            available in web interfaces.
        meta
            Arbitrary `key:value` pairs to associate with a query.
        context
            Deprecated in favor of `environment` and `tags`.

        Returns
        -------
        BulkOnlineQueryResponse
            An output containing results: list[BulkOnlineQueryResult], where each result contains dataframes of the
            results of each query.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        ... ChalkClient().query_bulk(
        ...     input={User.name: ["Katherine Johnson", "Eleanor Roosevelt"]},
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        """
        ...

    def plan_query(
        self,
        input: Sequence[FeatureReference],
        output: Sequence[FeatureReference],
        staleness: Mapping[FeatureReference, str] | None = None,
        environment: EnvironmentId | None = None,
        tags: list[str] | None = None,
        preview_deployment_id: str | None = None,
        branch: Union[BranchId, None] = ...,
        query_name: str | None = None,
        query_name_version: str | None = None,
        meta: Mapping[str, str] | None = None,
    ) -> PlanQueryResponse:
        """Plan a query without executing it.

        Parameters
        ----------
        input
            The features for which there are known values, mapped to those values.
            For example, `{User.id: 1234}`. Features can also be expressed as snakecased strings,
            e.g. `{"user.id": 1234}`
        output
            Outputs are the features that you'd like to compute from the inputs.
            For example, `[User.age, User.name, User.email]`.
        staleness
            Maximum staleness overrides for any output features or intermediate features.
            See https://docs.chalk.ai/docs/query-caching for more information.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the relevant preview deployment.
        query_name
            The semantic name for the query you're making, for example, `"loan_application_model"`.
            Typically, each query that you make from your application should have a name.
            Chalk will present metrics and dashboard functionality grouped by 'query_name'.
        meta
            Arbitrary `key:value` pairs to associate with a query.
        context
            Deprecated in favor of `environment` and `tags`.

        Returns
        -------
        PlanQueryResponse
            The query plan, including the resolver execution order and the
            resolver execution plan for each resolver.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> result = ChalkClient().plan_query(
        ...     input=[User.id],
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        >>> result.rendered_plan
        >>> result.output_schema
        """
        ...

    def offline_query(
        self,
        input: Mapping[FeatureReference, Any] | pd.DataFrame | pl.DataFrame | DataFrame | None = None,
        input_times: Sequence[datetime] | datetime | None = None,
        output: Sequence[FeatureReference] = (),
        required_output: Sequence[FeatureReference] = (),
        environment: EnvironmentId | None = None,
        dataset_name: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        max_samples: int | None = None,
        wait: bool = True,
        show_progress: bool = True,
        timeout: float | timedelta | ellipsis | None = ...,
        recompute_features: bool | list[FeatureReference] = False,
        sample_features: list[FeatureReference] | None = None,
        lower_bound: datetime | None = None,
        upper_bound: datetime | None = None,
        store_plan_stages: bool = False,
        explain: bool | Literal["only"] = False,
        tags: list[str] | None = None,
        required_resolver_tags: list[str] | None = None,
        planner_options: Mapping[str, Union[str, int, bool]] | None = None,
        spine_sql_query: str | None = None,
        spine_sql_primary_key_column_name: str | None = None,
    ) -> Dataset:
        """Compute feature values from the offline store or by running offline/online resolvers.
        See `Dataset` for more information.

        Parameters
        ----------
        input
            The features for which there are known values.
            It can be a mapping of features to a list of values for each
            feature, or an existing `DataFrame`.
            Each element in the `DataFrame` or list of values represents
            an observation in line with the timestamp in `input_times`.
        input_times
            A list of the times of the observations from `input`.
        output
            The features that you'd like to sample, if they exist.
            If an output feature was never computed for a sample (row) in
            the resulting `DataFrame`, its value will be `None`.
        recompute_features
            Used to control whether or not resolvers are allowed to run in order to compute feature values.

            If True, all output features will be recomputed by resolvers.
            If False, all output features will be sampled from the offline store.
            If a list, all output features in recompute_features will be recomputed,
            and all other output features will be sampled from the offline store.
        sample_features
            A list of features that will always be sampled, and thus always excluded from recompute.
            Should not overlap with any features used in "recompute_features" argument.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        dataset_name
            A unique name that if provided will be used to generate and
            save a `Dataset` constructed from the list of features computed
            from the inputs.
        max_samples
            The maximum number of samples to include in the `DataFrame`.
            If not specified, all samples will be returned.
        branch
            If specified, Chalk will route your request to the relevant branch.
            If None, Chalk will route your request to a non-branch deployment.
            If not specified, Chalk will use the current client's branch info.
        correlation_id
            You can specify a correlation ID to be used in logs and web interfaces.
            This should be globally unique, i.e. a `uuid` or similar. Logs generated
            during the execution of your query will be tagged with this correlation id.
        wait
            Whether to wait for job completion
        show_progress
            If True, progress bars will be shown while the query is running.
            Primarily intended for use in a Jupyter-like notebook environment.
            This flag will also be propagated to the methods of the resulting
            `Dataset`.
        timeout:
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        lower_bound
            If specified, the query will only be run on data observed after this timestamp
        upper_bound
            If specified, the query will only be run on data observed before this timestamp
        store_plan_stages
            If True, the output of each of the query plan stages will be stored
            in S3/GCS. This will dramatically impact the performance of the query,
            so it should only be used for debugging.
            These files will be visible in the web dashboard's query detail view, and
            can be downloaded in full by clicking on a plan node in the query plan visualizer.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        required_resolver_tags
            If specified, *all* required_resolver_tags must be present on a resolver for it to be
            considered eligible to execute.
            See https://docs.chalk.ai/docs/resolver-tags for more information.

        Other Parameters
        ----------------
        required_output
            The features that you'd like to sample and must exist
            in each resulting row. Rows where a `required_output`
            was never stored in the offline store will be skipped.
            This differs from specifying the feature in `output`,
            where instead the row would be included, but the feature
            value would be `None`.

        Returns
        -------
        Dataset
            A Chalk `Dataset`.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> uids = [1, 2, 3, 4]
        >>> at = datetime.now()
        >>> dataset = ChalkClient().offline_query(
        ...     input={
        ...         User.id: uids,
        ...         User.ts: [at] * len(uids),
        ...     },
        ...     output=[
        ...         User.id,
        ...         User.fullname,
        ...         User.email,
        ...         User.name_email_match_score,
        ...     ],
        ...     dataset_name='my_dataset'
        ... )
        >>> df = dataset.get_data_as_pandas()
        """
        ...

    def get_dataset(
        self,
        dataset_name: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
        *,
        dataset_id: str | uuid.UUID | None = None,
        revision_id: str | uuid.UUID | None = None,
        job_id: str | uuid.UUID | None = None,
    ) -> Dataset:
        """Get a Chalk `Dataset` containing data from a previously created dataset.

        If an offline query has been created with a dataset name, `.get_dataset` will
        return a Chalk `Dataset`.
        The `Dataset` wraps a lazily-loading Chalk `DataFrame` that enables us to analyze
        our data without loading all of it directly into memory.
        See https://docs.chalk.ai/docs/training-client for more information.

        Parameters
        ----------
        dataset_name
            The name of the `Dataset` to return.
            Previously, you must have supplied a dataset name upon an offline query.
            Dataset names are unique for each environment.
            If 'dataset_name' is provided, then 'job_id' should not be provided.
        dataset_id
            A UUID returned in the `Dataset` object from an offline query.
            Dataset ids are unique for each environment.
            If 'dataset_id' is provided, then 'dataset_name' and 'revision_id' should not be provided.
        revision_id
            The unique id of the `DatasetRevision` to return.
            If a previously-created dataset did not have a name, you can look it
            up using its unique job id instead.
            If 'revision_id' is provided, then 'dataset_name' and 'dataset_id' should not be provided.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.

        Other Parameters
        ----------------
        job_id
            Same as revision id. Deprecated.

        Returns
        -------
        Dataset
            A `Dataset` that lazily loads your query data.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> uids = [1, 2, 3, 4]
        >>> at = datetime.now()
        >>> X = ChalkClient().offline_query(
        ...     input={
        ...         User.id: uids,
        ...         User.ts: [at] * len(uids),
        ...     },
        ...     output=[
        ...         User.id,
        ...         User.fullname,
        ...         User.email,
        ...         User.name_email_match_score,
        ...     ],
        ...     dataset='my_dataset_name'
        ... )

        Some time later...

        >>> dataset = ChalkClient().get_dataset(
        ...     dataset_name='my_dataset_name'
        ... )
        ...

        or

        >>> dataset = ChalkClient().get_dataset(
        ...     job_id='00000000-0000-0000-0000-000000000000'
        ... )
        ...

        If memory allows:

        >>> df: pd.DataFrame = dataset.get_data_as_pandas()
        """
        ...

    def trigger_resolver_run(
        self,
        resolver_fqn: str,
        environment: EnvironmentId | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
        upper_bound: datetime | None = None,
        lower_bound: datetime | None = None,
        store_online: bool = True,
        store_offline: bool = True,
        timestamping_mode: Literal["feature_time", "online_store_write_time"] = "feature_time",
    ) -> ResolverRunResponse:
        """Triggers a resolver to run.
        See https://docs.chalk.ai/docs/runs for more information.

        Parameters
        ----------
        resolver_fqn
            The fully qualified name of the resolver to trigger.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.
        upper_bound
            If specified, the resolver will only ingest data observed before this timestamp.
        lower_bound
            If specified, the resolver will only ingest data observed after this timestamp.
        store_online
            If True, the resolver run output will be stored in the online store.
        store_offline
            If True, the resolver run output will be stored in the offline store.
        branch

        Returns
        -------
        ResolverRunResponse
            Status of the resolver run and the run ID.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().trigger_resolver_run(
        ...     resolver_fqn="mymodule.fn"
        ... )
        """
        ...

    def get_run_status(
        self,
        run_id: str,
        environment: EnvironmentId | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
    ) -> ResolverRunResponse:
        """Retrieves the status of a resolver run.
        See https://docs.chalk.ai/docs/runs for more information.

        Parameters
        ----------
        run_id
            ID of the resolver run to check.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.
        branch

        Returns
        -------
        ResolverRunResponse
            Status of the resolver run and the run ID.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().get_run_status(
        ...     run_id="3",
        ... )
        ResolverRunResponse(
            id="3",
            status=ResolverRunStatus.SUCCEEDED
        )
        """
        ...

    def whoami(self) -> WhoAmIResponse:
        """Checks the identity of your client.

        Useful as a sanity test of your configuration.

        Returns
        -------
        WhoAmIResponse
            The identity of your client.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().whoami()
        WhoAmIResponse(user="...", environment_id='...', team_id='...')
        """
        ...

    def delete_features(
        self,
        namespace: str,
        features: list[str] | None,
        tags: list[str] | None,
        primary_keys: list[str],
    ) -> FeatureObservationDeletionResponse:
        """Targets feature observation values for deletion and performs deletion online and offline.

        Parameters
        ----------
        namespace
            The namespace in which the target features reside.
        features
            An optional list of the feature names of the features that should be deleted
            for the targeted primary keys. Not specifying this and not specifying the "tags" field
            will result in all features being targeted for deletion for the specified primary keys.
            Note that this parameter and the "tags" parameter are mutually exclusive.
        tags
            An optional list of tags that specify features that should be targeted for deletion.
            If a feature has a tag in this list, its observations for the primary keys you listed
            will be targeted for deletion. Not specifying this and not specifying the "features"
            field will result in all features being targeted for deletion for the specified primary
            keys. Note that this parameter and the "features" parameter are mutually exclusive.
        primary_keys
            The primary keys of the observations that should be targeted for deletion.

        Returns
        -------
        FeatureObservationDeletionResponse
            Holds any errors (if any) that occurred during the drop request.
            Deletion of a feature may partially-succeed.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().delete_features(
        ...     namespace="user",
        ...     features=["name", "email", "age"],
        ...     primary_keys=[1, 2, 3]
        ... )
        """
        ...

    def drop_features(self, namespace: str, features: list[str]) -> FeatureDropResponse:
        """
        Performs a drop on features, which involves a deletes all their data
        (both online and offline). Once the feature is reset in this manner,
        its type can be changed.

        Parameters
        ----------
        namespace
            The namespace in which the target features reside.
        features
            A list of the feature names of the features that should be dropped.

        Returns
        -------
        FeatureDropResponse
            Holds any errors (if any) that occurred during the drop request.
            Dropping a feature may partially-succeed.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().drop_features(
        ...     namespace="user",
        ...     features=["name", "email", "age"],
        ... )
        """
        ...

    def upload_features(
        self,
        input: Mapping[FeatureReference, Any],
        branch: BranchId | None = ...,
        environment: EnvironmentId | None = None,
        preview_deployment_id: str | None = None,
        correlation_id: str | None = None,
        query_name: str | None = None,
        meta: Mapping[str, str] | None = None,
    ) -> list[ChalkError] | None:
        """Upload data to Chalk for use in offline resolvers or to prime a cache.

        Parameters
        ----------
        input
            The features for which there are known values, mapped to those values.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        preview_deployment_id
            If specified, Chalk will route your request to the relevant preview deployment
        query_name
            Optionally associate this upload with a query name. See `.query` for more information.

        Other Parameters
        ----------------
        correlation_id
            A globally unique ID for this operation, used alongside logs and
            available in web interfaces.
        meta
            Arbitrary `key:value` pairs to associate with a query.
        branch
            If specified, Chalk will route your request to the relevant branch.

        Returns
        -------
        list[ChalkError] | None
            The errors encountered from uploading features.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().upload_features(
        ...     input={
        ...         User.id: 1,
        ...         User.name: "Katherine Johnson"
        ...     }
        ... )
        """
        ...

    def multi_upload_features(
        self,
        input: Union[
            list[Mapping[str | Feature | Any, Any]],
            Mapping[str | Feature | Any, list[Any]],
            pd.DataFrame,
            pl.DataFrame,
            DataFrame,
        ],
        branch: BranchId | None = ...,
        environment: EnvironmentId | None = None,
        preview_deployment_id: str | None = None,
        correlation_id: str | None = None,
        meta: Mapping[str, str] | None = None,
    ) -> list[ChalkError] | None:
        """Upload data to Chalk for use in offline resolvers or to prime a cache.

        Parameters
        ----------
        input
            A list of mappings, each of which includes the features for which there are known values mapped to
            those values. Each mapping can have different keys, but each mapping must have the same root features
            class.
                OR
            A mapping where each feature key is mapped to a list of the values for that feature. You can consider this
            a mapping that describes columns (keys, i.e. features) and rows (the list of values in the map for each
            feature). Each list must be the same length.
                OR
            A pandas, polars or Chalk DataFrame.
        branch
        environment
            The environment under which to run the upload.
            API tokens can be scoped to an environment.
            If no environment is specified in the upload,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        preview_deployment_id
            If specified, Chalk will route your request to the relevant preview deployment

        Other Parameters
        ----------------
        correlation_id
            A globally unique ID for this operation, used alongside logs and
            available in web interfaces. If None, a correlation ID will be
            generated for you and returned on the response.
        meta
            Arbitrary key:value pairs to associate with an upload.

        Returns
        -------
        list[ChalkError] | None
            The errors encountered from uploading features.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().multi_upload_features(
        ...     input=[
        ...         {
        ...             User.id: 1,
        ...             User.name: "Katherine Johnson"
        ...         },
        ...         {
        ...             User.id: 2,
        ...             User.name: "Eleanor Roosevelt"
        ...         }
        ...     ]
        ... )
        """
        ...

    def sample(
        self,
        output: Sequence[FeatureReference] = (),
        required_output: Sequence[FeatureReference] = (),
        output_id: bool = False,
        output_ts: Union[bool, str] = False,
        max_samples: int | None = None,
        dataset: str | None = None,
        branch: BranchId | None = None,
        environment: EnvironmentId | None = None,
        tags: list[str] | None = None,
    ) -> pd.DataFrame:
        """Get the most recent feature values from the offline store.

        See https://docs.chalk.ai/docs/training-client for more information.

        Parameters
        ----------
        output
            The features that you'd like to sample, if they exist.
            If an output feature was never computed for a sample (row)
            in the resulting `DataFrame`, its value will be `None`.
        max_samples
            The maximum number of rows to return.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        dataset
            The `Dataset` name under which to save the output.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.

        Other Parameters
        ----------------
        required_output
            The features that you'd like to sample and must exist
            in each resulting row. Rows where a `required_output`
            was never stored in the offline store will be skipped.
            This differs from specifying the feature in `output`,
            where instead the row would be included, but the feature
            value would be `None`.
        output_ts
            Whether to return the input-time feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `DataFrame`.
            If set to a non-empty `str`, used as the input-time column name.
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        branch

        Returns
        -------
        pd.DataFrame
            A `pandas.DataFrame` with columns equal to the names of the features in output,
            and values representing the value of the most recent observation.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> sample_df = ChalkClient().sample(
        ...     output=[
        ...         Account.id,
        ...         Account.title,
        ...         Account.user.full_name
        ...     ],
        ...     max_samples=10
        ... )
        """
        ...

    def create_branch(
        self,
        branch_name: str,
        create_only: bool = False,
        switch: bool = True,
        source_deployment_id: str | None = None,
        environment: EnvironmentId | None = None,
    ) -> BranchDeployResponse:
        """
        Create a new branch based off of a deployment from the server.
        By default, uses the latest live deployment.

        Parameters
        ----------
        branch_name
            The name of the new branch to create.
        create_only
            If `True`, will raise an error if a branch with the given
            name already exists. If `False` and the branch exists, then
            that branch will be deployed to.
        switch
            If `True`, will switch the client to the newly created branch.
            Defaults to `True`.
        source_deployment_id
            The specific deployment ID to use for the branch.
            If not specified, the latest live deployment on the
            server will be used. You can see which deployments
            are available by clicking on the 'Deployments' tab on
            the project page in the Chalk dashboard.
        environment
            The environment under which to create the branch. API
            tokens can be scoped to an environment. If no environment
            is specified in the query, the environment will be taken
            from the client's cached token.

        Returns
        -------
        BranchDeployResponse
            A response object containing metadata about the branch.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient()
        >>> client.create_branch("my-new-branch")
        """
        ...

    def get_branches(self) -> list[str]:
        """Lists the current branches for this environment.

        Returns
        -------
        list[str]
            A list of the names of branches available on this environment.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().get_branches()
        ["testing", "feat/new-feature"]
        """
        ...

    def get_branch(self) -> str | None:
        """Displays the current branch this client is pointed at.

        If the current environment does not support branch deployments
        or no branch is set, this method returns `None`.

        Returns
        -------
        str | None
            The name of the current branch or `None`.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient(branch="my-branch")
        >>> assert client.get_branch() == "my-branch"
        """
        ...

    def set_branch(self, branch_name: Optional[str]):
        """Point the `ChalkClient` at the given branch.
        If `branch_name` is None, this points the client at the
        active non-branch deployment.

        If the branch does not exist or if branch deployments
        are not enabled for the current environment, this
        method raises an error.

        Parameters
        ----------
        branch_name
            The name of the branch to use, or None

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient()
        >>> client.create_branch("my-new-branch")
        >>> client.set_branch("my-new-branch")
        >>> client.set_branch(None)
        """
        ...

    def reset_branch(self, branch: BranchIdParam = ..., environment: EnvironmentId | None = None):
        ...

    def branch_state(
        self,
        branch: BranchId | ellipsis = ...,
        environment: EnvironmentId | None = None,
    ) -> BranchGraphSummary:
        """
        Returns a `BranchGraphSummary` object that contains the
        state of the branch server: Which resolver/features are
        defined, and the history of live notebook updates on the
        server.

        Parameters
        ----------
        branch
            The branch to query. If not specified, the branch is
            expected to be included in the constructor for `ChalkClient`.
        environment
            Optionally override the environment under which to query the branch state.
        """
        ...

    def set_incremental_cursor(
        self,
        *,
        resolver: str | Resolver | None = None,
        scheduled_query: str | None = None,
        max_ingested_timestamp: datetime | None = None,
        last_execution_timestamp: datetime | None = None,
    ) -> None:
        """
        Sets the incremental cursor for a resolver or scheduled query.

        Parameters
        ---------
        resolver
            The resolver. Can be a function or the string name of a function.
            Exactly one of `resolver` and `scheduled_query` is required.
        scheduled_query
            The name of the scheduled query. Exactly one of `resolver` and `scheduled_query`
            is required.
        max_ingested_timestamp
            Set the maximum timestamp of the data ingested by the resolver.
        last_execution_timestamp
            Override the last execution timestamp of the resolver.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient()
        >>> client.set_incremental_cursor(
        ...     resolver="my_resolver",
        ...     max_ingested_timestamp=datetime.now(),
        ... )
        """
        ...

    def get_incremental_cursor(
        self,
        *,
        resolver: str | Resolver | None = None,
        scheduled_query: str | None = None,
    ) -> GetIncrementalProgressResponse:
        """
        Gets the incremental cursor for a resolver or scheduled query.

        Parameters
        ---------
        resolver
            The resolver. Can be a function or the string name of a function.
            Exactly one of `resolver` and `scheduled_query` is required.
        scheduled_query
            If updating incremental status of a resolver in the context of a
            scheduled query, the name of the scheduled query.
            Exactly one of `resolver` and `scheduled_query` is required.

        Returns
        ------
        IncrementalStatus
            An object containing the `max_ingested_timestamp` and `incremental_timestamp`.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient()
        >>> client.get_incremental_cursor(resolver="my_resolver")
        """
        ...

    def test_streaming_resolver(
        self,
        resolver: str | Resolver,
        num_messages: int | None = None,
        message_filepath: str | None = None,
        message_keys: list[str] | None = None,
        message_bodies: list[str | bytes] | None = None,
        message_timestamps: list[str | datetime] | None = None,
        branch: BranchId | ellipsis = ...,
        environment: EnvironmentId | None = None,
    ) -> StreamResolverTestResponse:
        """
        Tests a streaming resolver and its ability to parse and resolve messages.
        See https://docs.chalk.ai/docs/streams for more information.

        Parameters
        ----------
        resolver
            The streaming resolver or its string name.
        num_messages
            The number of messages to digest from the stream source.
            As messages may not be incoming into the stream, this action may time out.
        message_filepath
            A filepath from which test messages will be ingested.
            This file should be newline delimited json as follows:

            >>> {"message_key": "my-key", "message_body": {"field1": "value1", "field2": "value2"}}
            >>> {"message_key": "my-key", "message_body": {"field1": "value1", "field2": "value2"}}

            Each line may optionally contain a timezone string as a value to the key "message_timestamp".
        message_keys
            Alternatively, keys can be supplied in code along with the "test_message_bodies" argument.
            Both arguments must be the same length.
        message_bodies
            Message bodies can be supplied in code as strings or bytes along with the "test_message_keys" argument.
            Both arguments must be the same length.
        message_timestamps
            Optionally, timestamps can be provided for each message,

        Other Parameters
        ----------
        branch
            If specified, Chalk will route your request to the relevant branch.
        environment
            The environment under which to create the branch. API
            tokens can be scoped to an environment. If no environment
            is specified in the query, the environment will be taken
            from the client's cached token.

        Returns
        -------
        StreamResolverTestResponse
            A simple wrapper around a status and optional error message.
            Inspecting `StreamResolverTestResponse.features` will return the test results, if they exist.
            Otherwise, check `StreamResolverTestResponse.errors` and `StreamResolverTestResponse.message` for errors.

        Examples
        --------
        >>> from chalk.streams import stream, KafkaSource
        >>> from chalk.client import ChalkClient
        >>> from chalk.features import Features, features
        >>> import pydantic
        >>> # This code is an example of a simple streaming feature setup. Define the source
        >>> stream_source=KafkaSource(...)
        >>> # Define the features
        >>> @features(etl_offline_to_online=True, max_staleness="7d")
        >>> class StreamingFeature:
        >>>     id: str
        >>>     user_id: str
        >>>     card_id: str
        >>> # Define the streaming message model
        >>> class StreamingMessage(pydantic.BaseModel):
        >>>     card_id: str
        >>>     user_id: str
        >>> # Define the mapping resolver
        >>> @stream(source=stream_source)
        >>> def our_stream_resolver(
        >>>     m: StreamingMessage,
        >>> ) -> Features[StreamingFeature.id, StreamingFeature.card_id, StreamingFeature.user_id]:
        >>>    return StreamingFeature(
        >>>        id=f"{m.card_id}-{m.user_id}",
        >>>        card_id=m.card_id,
        >>>        user_id=m.user_id,
        >>>    )
        >>> # Once you have done a `chalk apply`, you can test the streaming resolver with custom messages as follows
        >>> client = ChalkClient()
        >>> keys = ["my_key"] * 10
        >>> messages = [StreamingMessage(card_id="1", user_id=str(i)).json() for i in range(10)]
        >>> resp = client.test_streaming_resolver(
        >>>     resolver="our_stream_resolver",
        >>>     message_keys=keys,
        >>>     message_bodies=messages,
        >>> )
        >>> print(resp.features)
        """
        ...

    def __new__(cls, *args: Any, **kwargs: Any):
        from chalk.client.client_impl import ChalkAPIClientImpl

        return ChalkAPIClientImpl.__new__(cls, *args, **kwargs)


class AsyncChalkClient:
    """The `AsyncChalkClient` is an asynchronous Python interface for interacting with Chalk.

    You can use it to query data, trigger resolver runs, gather offline data, and more, and all calls are asynchronous.
    """

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
        api_server: Optional[str] = None,
        query_server: Optional[str] = None,
        branch: Optional[BranchId] = None,
        preview_deployment_id: Optional[DeploymentId] = None,
        additional_headers: Optional[Mapping[str, str]] = None,
        default_job_timeout: float | timedelta | None = None,
        executor: Optional[ThreadPoolExecutor] = None,
    ):
        """Create an `AsyncChalkClient` with the given credentials.

        Parameters
        ----------
        client_id
            The client ID to use to authenticate. Can either be a
            service token id or a user token id.
        client_secret
            The client secret to use to authenticate. Can either be a
            service token secret or a user token secret.
        environment
            The ID or name of the environment to use for this client.
            Not necessary if your `client_id` and `client_secret`
            are for a service token scoped to a single environment.
            If not present, the client will use the environment variable
            `CHALK_ENVIRONMENT`.
        api_server
            The API server to use for this client. Required if you are
            using a Chalk Dedicated deployment. If not present, the client
            will check for the presence of the environment variable
            `CHALK_API_SERVER`, and use that if found.
        query_server
            The query server to use for this client. Required if you are
            using a standalone Chalk query engine deployment. If not present,
            the client will default to the value of api_server.
        branch
            If specified, Chalk will route all requests from this client
            instance to the relevant branch. Some methods allow you to
            override this instance-level branch configuration by passing
            in a `branch` argument.
        preview_deployment_id
            If specified, Chalk will route all requests from this client
            instance to the relevant preview deployment.
        additional_headers
            A map of additional HTTP headers to pass with each request.
        default_job_timeout
            The default wait timeout, in seconds, to wait for long-running jobs to complete
            when accessing query results.
            Jobs will not timeout if this timeout elapses. For no timeout, set to None.
            The default timeout is 10 minutes.
        executor
            A custom `ThreadPoolExecutor` to use for running asynchronous tasks. If not provided,
            will use Chalk's default thread pool.
        Raises
        ------
        ChalkAuthException
            If `client_id` or `client_secret` are not provided, there
            is no `~/.chalk.yml` file with applicable credentials,
            and the environment variables `CHALK_CLIENT_ID` and
            `CHALK_CLIENT_SECRET` are not set.
        """
        super().__init__()
        ...

    def __new__(cls, *args: Any, **kwargs: Any):
        from chalk.client.client_async import AsyncChalkClientImpl

        return AsyncChalkClientImpl.__new__(cls, *args, **kwargs)

    async def query(
        self,
        input: Mapping[FeatureReference, Any] | Any,
        output: Sequence[FeatureReference] = (),
        now: datetime | None = None,
        staleness: Mapping[FeatureReference, str] | None = None,
        environment: EnvironmentId | None = None,
        tags: list[str] | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        query_name: str | None = None,
        query_name_version: str | None = None,
        include_meta: bool = False,
        meta: Mapping[str, str] | None = None,
        explain: bool | Literal["only"] = False,
        store_plan_stages: bool = False,
        encoding_options: FeatureEncodingOptions | None = None,
        required_resolver_tags: list[str] | None = None,
        planner_options: Mapping[str, Union[str, int, bool]] | None = None,
        request_timeout: Optional[float] = None,
    ) -> OnlineQueryResult:
        """Compute features values using online resolvers.
        See https://docs.chalk.ai/docs/query-basics for more information.

        Parameters
        ----------
        input
            The features for which there are known values, mapped to those values.
            For example, `{User.id: 1234}`. Features can also be expressed as snakecased strings,
            e.g. `{"user.id": 1234}`
        output
            Outputs are the features that you'd like to compute from the inputs.
            For example, `[User.age, User.name, User.email]`.

            If an empty sequence, the output will be set to all features on the namespace
            of the query. For example, if you pass as input `{"user.id": 1234}`, then the query
            is defined on the `User` namespace, and all features on the `User` namespace
            (excluding has-one and has-many relationships) will be used as outputs.
        staleness
            Maximum staleness overrides for any output features or intermediate features.
            See https://docs.chalk.ai/docs/query-caching for more information.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        required_resolver_tags
            If specified, *all* required_resolver_tags must be present on a resolver for it to be
            considered eligible to execute.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the relevant preview deployment.
        query_name
            The semantic name for the query you're making, for example, `"loan_application_model"`.
            Typically, each query that you make from your application should have a name.
            Chalk will present metrics and dashboard functionality grouped by 'query_name'.
        include_meta
            Returns metadata about the query execution under `OnlineQueryResult.meta`.
            This could make the query slightly slower.
            For more information, see https://docs.chalk.ai/docs/query-basics.
        explain
            Log the query execution plan. Requests using `explain=True` will be slower
            than requests using `explain=False`. If `"only"`, the query will not be executed,
            and only the query plan will be returned.

            If `True`, 'include_meta' will be set to `True` as well.
        store_plan_stages
            If `True`, the output of each of the query plan stages will be stored.
            This option dramatically impacts the performance of the query,
            so it should only be used for debugging.
        correlation_id
            You can specify a correlation ID to be used in logs and web interfaces.
            This should be globally unique, i.e. a `uuid` or similar. Logs generated
            during the execution of your query will be tagged with this correlation id.
        now
            The time at which to evaluate the query. If not specified, the current time will be used.
            This parameter is complex in the context of online_query since the online store
            only stores the most recent value of an entity's features. If `now` is in the past,
            it is extremely likely that `None` will be returned for cache-only features.

            This parameter is primarily provided to support:
                - controlling the time window for aggregations over cached has-many relationships
                - controlling the time wnidow for aggregations over has-many relationships loaded from an
                  external database

            If you are trying to perform an exploratory analysis of past feature values, prefer `offline_query`.

        Other Parameters
        ----------------
        meta
            Arbitrary `key:value` pairs to associate with a query.

        planner_options
            Dictionary of additional options to pass to the Chalk query engine.
            Values may be provided as part of conversations with Chalk support to
            to enable or disable specific functionality.

        request_timeout
            Float value indicating number of seconds that the request should wait before timing out
            at the network level. May not cancel resources on the server processing the query.

        Returns
        -------
        Awaitable[OnlineQueryResult]
            Coroutine that returns a wrapper around the output features and any query metadata,
            plus errors encountered while running the resolvers.

        Examples
        --------
        >>> from chalk.client import AsyncChalkClient
        >>> result = await AsyncChalkClient().query(
        ...     input={
        ...         User.name: "Katherine Johnson"
        ...     },
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        >>> result.get_feature_value(User.fico_score)
        """
        ...

    async def multi_query(
        self,
        queries: list[OnlineQuery],
        environment: EnvironmentId | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        query_name: str | None = None,
        query_name_version: str | None = None,
        meta: Mapping[str, str] | None = None,
        use_feather: bool | None = True,
        compression: str | None = "uncompressed",
    ) -> BulkOnlineQueryResponse:
        """
        Execute multiple queries (represented by `queries=` argument) in a single request. This is useful if the
        queries are "rooted" in different `@features` classes -- i.e. if you want to load features for `User` and
        `Merchant` and there is no natural relationship object which is related to both of these classes, `multi_query`
        allows you to submit two independent queries.

        Returns a BulkOnlineQueryResponse, which is functionally a list of query results. Each of these result
        can be accessed by index. Individual results can be further checked for errors and converted
        to pandas or polars DataFrames.

        In contrast, `query_bulk` executes a single query with multiple inputs/outputs.

        Parameters
        ----------
        queries
            A list of the OnlineQueries you'd like to execute.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.

        Other Parameters
        ----------------
        query_name
            The name for class of query you're making, for example, `"loan_application_model"`.
        correlation_id
            A globally unique ID for the query, used alongside logs and
            available in web interfaces.
        meta
            Arbitrary `key:value` pairs to associate with a query.
        compression
            Which compression scheme to use pyarrow. Options are: {"zstd", "lz4", "uncompressed"}.

        Returns
        -------
        Awaitable[BulkOnlineQueryResponse]
            Coroutine that returns object containing results: list[BulkOnlineQueryResult], where each result contains
            dataframes of the results of each query or any errors.

        Examples
        --------
        >>> from chalk.client import AsyncChalkClient, OnlineQuery
        >>> queries =[
        ...     OnlineQuery(input={User.name: ['Katherine Johnson'], output=[User.fico_score]}),
        ...     OnlineQuery(input={Merchant.name': ['Myrrh Chant'], output=['Merchant.address']}),
        ...     OnlineQuery(input={NonFeature.wrong': ['Wrong!'], output=['NonFeature.wrong']}),
        ... ]
        >>> result = await AsyncChalkClient().multi_query(
        ...     queries=queries,
        ... )
        >>> result[0].get_feature_value(User.fico_score)
        >>> queries_with_errors = [q for q, r in zip(queries, result) if r.errors is not None]
        """
        ...

    async def query_bulk(
        self,
        input: Mapping[FeatureReference, Sequence[Any]],
        output: Sequence[FeatureReference],
        now: Sequence[datetime] | None = None,
        staleness: Mapping[FeatureReference, str] | None = None,
        context: OnlineQueryContext | None = None,  # Deprecated.
        environment: EnvironmentId | None = None,
        tags: list[str] | None = None,
        required_resolver_tags: list[str] | None = None,
        preview_deployment_id: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        query_name: str | None = None,
        query_name_version: str | None = None,
        meta: Mapping[str, str] | None = None,
    ) -> BulkOnlineQueryResponse:
        """Compute features values for many rows of inputs using online resolvers.
        See https://docs.chalk.ai/docs/query-basics for more information on online query.

        This method is similar to `query`, except it takes in `list` of inputs, and produces one
        output per row of inputs.

        This method is appropriate if you want to fetch the same set of features for many different
        input primary keys.

        This method contrasts with `multi_query`, which executes multiple fully independent queries.

        This endpoint is not available in all environments.


        Parameters
        ----------
        input
            The features for which there are known values, mapped to a list
            of the values.
        output
            Outputs are the features that you'd like to compute from the inputs.
        staleness
            Maximum staleness overrides for any output features or intermediate features.
            See https://docs.chalk.ai/docs/query-caching for more information.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.
        now
            The time at which to evaluate the query. If not specified, the current time will be used.
            The length of this list must be the same as the length of the values in `input`.

        Other Parameters
        ----------------
        query_name
            The name for class of query you're making, for example, `"loan_application_model"`.
        correlation_id
            A globally unique ID for the query, used alongside logs and
            available in web interfaces.
        meta
            Arbitrary `key:value` pairs to associate with a query.
        context
            Deprecated in favor of `environment` and `tags`.

        Returns
        -------
        Awaitable[BulkOnlineQueryResponse]
            Coroutine of a list[BulkOnlineQueryResult], where each result contains dataframes of the
            results of each query.

        Examples
        --------
        >>> from chalk.client import AsyncChalkClient
        ... await AsyncChalkClient().query_bulk(
        ...     input={User.name: ["Katherine Johnson", "Eleanor Roosevelt"]},
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        """
        ...

    async def offline_query(
        self,
        input: Mapping[FeatureReference, Any] | pd.DataFrame | pl.DataFrame | DataFrame | None = None,
        input_times: Sequence[datetime] | datetime | None = None,
        output: Sequence[FeatureReference] = (),
        required_output: Sequence[FeatureReference] = (),
        environment: EnvironmentId | None = None,
        dataset_name: str | None = None,
        branch: BranchId | None = ...,
        correlation_id: str | None = None,
        max_samples: int | None = None,
        wait: bool = True,
        show_progress: bool = True,
        timeout: float | timedelta | ellipsis | None = ...,
        recompute_features: bool | list[FeatureReference] = False,
        sample_features: list[FeatureReference] | None = None,
        lower_bound: datetime | None = None,
        upper_bound: datetime | None = None,
        store_plan_stages: bool = False,
        explain: bool | Literal["only"] = False,
        tags: list[str] | None = None,
        required_resolver_tags: list[str] | None = None,
        planner_options: Mapping[str, Union[str, int, bool]] | None = None,
        spine_sql_query: str | None = None,
        spine_sql_primary_key_column_name: str | None = None,
    ) -> Dataset:
        """Compute feature values from the offline store or by running offline/online resolvers.
        See `Dataset` for more information.

        Parameters
        ----------
        input
            The features for which there are known values.
            It can be a mapping of features to a list of values for each
            feature, or an existing `DataFrame`.
            Each element in the `DataFrame` or list of values represents
            an observation in line with the timestamp in `input_times`.
        input_times
            A list of the times of the observations from `input`.
        output
            The features that you'd like to sample, if they exist.
            If an output feature was never computed for a sample (row) in
            the resulting `DataFrame`, its value will be `None`.
        recompute_features
            Used to control whether or not resolvers are allowed to run in order to compute feature values.

            If True, all output features will be recomputed by resolvers.
            If False, all output features will be sampled from the offline store.
            If a list, all output features in recompute_features will be recomputed,
            and all other output features will be sampled from the offline store.
        sample_features
            A list of features that will always be sampled, and thus always excluded from recompute.
            Should not overlap with any features used in "recompute_features" argument.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        dataset_name
            A unique name that if provided will be used to generate and
            save a `Dataset` constructed from the list of features computed
            from the inputs.
        max_samples
            The maximum number of samples to include in the `DataFrame`.
            If not specified, all samples will be returned.
        branch
            If specified, Chalk will route your request to the relevant branch.
            If None, Chalk will route your request to a non-branch deployment.
            If not specified, Chalk will use the current client's branch info.
        correlation_id
            You can specify a correlation ID to be used in logs and web interfaces.
            This should be globally unique, i.e. a `uuid` or similar. Logs generated
            during the execution of your query will be tagged with this correlation id.
        wait
            Whether to wait for job completion
        show_progress
            If True, progress bars will be shown while the query is running.
            Primarily intended for use in a Jupyter-like notebook environment.
            This flag will also be propagated to the methods of the resulting
            `Dataset`.
        timeout:
            How long to wait, in seconds, for job completion before raising a TimeoutError.
            Jobs will continue to run in the background if they take longer than this timeout.
            For no timeout, set to ``None``. If no timeout is specified, the client's default
            timeout is used.
        lower_bound
            If specified, the query will only be run on data observed after this timestamp
        upper_bound
            If specified, the query will only be run on data observed before this timestamp
        store_plan_stages
            If True, the output of each of the query plan stages will be stored
            in S3/GCS. This will dramatically impact the performance of the query,
            so it should only be used for debugging.
            These files will be visible in the web dashboard's query detail view, and
            can be downloaded in full by clicking on a plan node in the query plan visualizer.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        required_resolver_tags
            If specified, *all* required_resolver_tags must be present on a resolver for it to be
            considered eligible to execute.
            See https://docs.chalk.ai/docs/resolver-tags for more information.

        Other Parameters
        ----------------
        required_output
            The features that you'd like to sample and must exist
            in each resulting row. Rows where a `required_output`
            was never stored in the offline store will be skipped.
            This differs from specifying the feature in `output`,
            where instead the row would be included, but the feature
            value would be `None`.

        Returns
        -------
        Dataset
            A Chalk `Dataset`.

        Examples
        --------
        >>> from chalk.client import AsyncChalkClient
        >>> uids = [1, 2, 3, 4]
        >>> at = datetime.now()
        >>> dataset = await AsyncChalkClient().offline_query(
        ...     input={
        ...         User.id: uids,
        ...         User.ts: [at] * len(uids),
        ...     },
        ...     output=[
        ...         User.id,
        ...         User.fullname,
        ...         User.email,
        ...         User.name_email_match_score,
        ...     ],
        ...     dataset_name='my_dataset'
        ... )
        >>> df = dataset.get_data_as_pandas()
        """
        ...


ChalkAPIClientProtocol: TypeAlias = ChalkClient
"""Deprecated. Use `ChalkClient` instead."""

__all__ = [
    "AsyncChalkClient",
    "ChalkAPIClientProtocol",
    "ChalkBaseException",
    "ChalkClient",
    "ChalkAuthException",
    "ChalkError",
    "ChalkException",
    "Dataset",
    "DatasetRevision",
    "ErrorCode",
    "ErrorCodeCategory",
    "FeatureResult",
    "OfflineQueryContext",
    "OnlineQuery",
    "OnlineQueryContext",
    "OnlineQueryResponse",
    "OnlineQueryResult",
    "QueryStatus",
    "ResolverRunResponse",
    "WhoAmIResponse",
    "Permission",
]

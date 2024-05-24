"""
Type annotations for emr-serverless service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_emr_serverless.client import EMRServerlessClient
    from mypy_boto3_emr_serverless.paginator import (
        ListApplicationsPaginator,
        ListJobRunsPaginator,
    )

    session = Session()
    client: EMRServerlessClient = session.client("emr-serverless")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    ```
"""

from typing import Generic, Iterator, Sequence, TypeVar

from botocore.paginate import PageIterator, Paginator

from .literals import ApplicationStateType, JobRunStateType
from .type_defs import (
    ListApplicationsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

__all__ = ("ListApplicationsPaginator", "ListJobRunsPaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListApplicationsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        states: Sequence[ApplicationStateType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> _PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listapplicationspaginator)
        """


class ListJobRunsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listjobrunspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        createdAtAfter: TimestampTypeDef = ...,
        createdAtBefore: TimestampTypeDef = ...,
        states: Sequence[JobRunStateType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> _PageIterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listjobrunspaginator)
        """

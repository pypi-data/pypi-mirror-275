# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkdis.v2.dis_client import DisClient
from huaweicloudsdkdis.v2.dis_async_client import DisAsyncClient

from huaweicloudsdkdis.v2.model.batch_create_tags_req import BatchCreateTagsReq
from huaweicloudsdkdis.v2.model.batch_create_tags_request import BatchCreateTagsRequest
from huaweicloudsdkdis.v2.model.batch_create_tags_response import BatchCreateTagsResponse
from huaweicloudsdkdis.v2.model.batch_delete_tags_req import BatchDeleteTagsReq
from huaweicloudsdkdis.v2.model.batch_delete_tags_request import BatchDeleteTagsRequest
from huaweicloudsdkdis.v2.model.batch_delete_tags_response import BatchDeleteTagsResponse
from huaweicloudsdkdis.v2.model.batch_start_transfer_task_req import BatchStartTransferTaskReq
from huaweicloudsdkdis.v2.model.batch_start_transfer_task_request import BatchStartTransferTaskRequest
from huaweicloudsdkdis.v2.model.batch_start_transfer_task_response import BatchStartTransferTaskResponse
from huaweicloudsdkdis.v2.model.batch_stop_transfer_task_req import BatchStopTransferTaskReq
from huaweicloudsdkdis.v2.model.batch_stop_transfer_task_request import BatchStopTransferTaskRequest
from huaweicloudsdkdis.v2.model.batch_stop_transfer_task_response import BatchStopTransferTaskResponse
from huaweicloudsdkdis.v2.model.batch_transfer_task import BatchTransferTask
from huaweicloudsdkdis.v2.model.csv_properties import CSVProperties
from huaweicloudsdkdis.v2.model.cloudtable_destination_descriptor_request import CloudtableDestinationDescriptorRequest
from huaweicloudsdkdis.v2.model.cloudtable_schema import CloudtableSchema
from huaweicloudsdkdis.v2.model.column import Column
from huaweicloudsdkdis.v2.model.commit_checkpoint_req import CommitCheckpointReq
from huaweicloudsdkdis.v2.model.commit_checkpoint_request import CommitCheckpointRequest
from huaweicloudsdkdis.v2.model.commit_checkpoint_response import CommitCheckpointResponse
from huaweicloudsdkdis.v2.model.common_destination_descriptor import CommonDestinationDescriptor
from huaweicloudsdkdis.v2.model.consume_records_request import ConsumeRecordsRequest
from huaweicloudsdkdis.v2.model.consume_records_response import ConsumeRecordsResponse
from huaweicloudsdkdis.v2.model.create_app_req import CreateAppReq
from huaweicloudsdkdis.v2.model.create_app_request import CreateAppRequest
from huaweicloudsdkdis.v2.model.create_app_response import CreateAppResponse
from huaweicloudsdkdis.v2.model.create_obs_transfer_task_request import CreateObsTransferTaskRequest
from huaweicloudsdkdis.v2.model.create_obs_transfer_task_response import CreateObsTransferTaskResponse
from huaweicloudsdkdis.v2.model.create_stream_req import CreateStreamReq
from huaweicloudsdkdis.v2.model.create_stream_request import CreateStreamRequest
from huaweicloudsdkdis.v2.model.create_stream_response import CreateStreamResponse
from huaweicloudsdkdis.v2.model.create_tag_req import CreateTagReq
from huaweicloudsdkdis.v2.model.create_tag_request import CreateTagRequest
from huaweicloudsdkdis.v2.model.create_tag_response import CreateTagResponse
from huaweicloudsdkdis.v2.model.create_transfer_task_req import CreateTransferTaskReq
from huaweicloudsdkdis.v2.model.dws_destination_descriptor_request import DWSDestinationDescriptorRequest
from huaweicloudsdkdis.v2.model.data_point import DataPoint
from huaweicloudsdkdis.v2.model.delete_app_request import DeleteAppRequest
from huaweicloudsdkdis.v2.model.delete_app_response import DeleteAppResponse
from huaweicloudsdkdis.v2.model.delete_checkpoint_request import DeleteCheckpointRequest
from huaweicloudsdkdis.v2.model.delete_checkpoint_response import DeleteCheckpointResponse
from huaweicloudsdkdis.v2.model.delete_stream_request import DeleteStreamRequest
from huaweicloudsdkdis.v2.model.delete_stream_response import DeleteStreamResponse
from huaweicloudsdkdis.v2.model.delete_tag_request import DeleteTagRequest
from huaweicloudsdkdis.v2.model.delete_tag_response import DeleteTagResponse
from huaweicloudsdkdis.v2.model.delete_transfer_task_request import DeleteTransferTaskRequest
from huaweicloudsdkdis.v2.model.delete_transfer_task_response import DeleteTransferTaskResponse
from huaweicloudsdkdis.v2.model.describe_app_result import DescribeAppResult
from huaweicloudsdkdis.v2.model.dli_destination_descriptor_request import DliDestinationDescriptorRequest
from huaweicloudsdkdis.v2.model.list_app_request import ListAppRequest
from huaweicloudsdkdis.v2.model.list_app_response import ListAppResponse
from huaweicloudsdkdis.v2.model.list_policies_request import ListPoliciesRequest
from huaweicloudsdkdis.v2.model.list_policies_response import ListPoliciesResponse
from huaweicloudsdkdis.v2.model.list_resource_instances_req import ListResourceInstancesReq
from huaweicloudsdkdis.v2.model.list_resources_by_tags_request import ListResourcesByTagsRequest
from huaweicloudsdkdis.v2.model.list_resources_by_tags_response import ListResourcesByTagsResponse
from huaweicloudsdkdis.v2.model.list_streams_request import ListStreamsRequest
from huaweicloudsdkdis.v2.model.list_streams_response import ListStreamsResponse
from huaweicloudsdkdis.v2.model.list_tags_request import ListTagsRequest
from huaweicloudsdkdis.v2.model.list_tags_response import ListTagsResponse
from huaweicloudsdkdis.v2.model.list_transfer_tasks_request import ListTransferTasksRequest
from huaweicloudsdkdis.v2.model.list_transfer_tasks_response import ListTransferTasksResponse
from huaweicloudsdkdis.v2.model.mrs_destination_descriptor_request import MRSDestinationDescriptorRequest
from huaweicloudsdkdis.v2.model.metrics import Metrics
from huaweicloudsdkdis.v2.model.obs_destination_descriptor_request import OBSDestinationDescriptorRequest
from huaweicloudsdkdis.v2.model.open_tsdb_metric import OpenTSDBMetric
from huaweicloudsdkdis.v2.model.open_tsdb_schema import OpenTSDBSchema
from huaweicloudsdkdis.v2.model.open_tsdb_tags import OpenTSDBTags
from huaweicloudsdkdis.v2.model.open_tsdb_timestamp import OpenTSDBTimestamp
from huaweicloudsdkdis.v2.model.open_tsdb_value import OpenTSDBValue
from huaweicloudsdkdis.v2.model.options import Options
from huaweicloudsdkdis.v2.model.partition_result import PartitionResult
from huaweicloudsdkdis.v2.model.principal_rule import PrincipalRule
from huaweicloudsdkdis.v2.model.processing_schema import ProcessingSchema
from huaweicloudsdkdis.v2.model.put_records_request import PutRecordsRequest
from huaweicloudsdkdis.v2.model.put_records_request_entry import PutRecordsRequestEntry
from huaweicloudsdkdis.v2.model.put_records_result_entry import PutRecordsResultEntry
from huaweicloudsdkdis.v2.model.record import Record
from huaweicloudsdkdis.v2.model.row_key import RowKey
from huaweicloudsdkdis.v2.model.send_records_request import SendRecordsRequest
from huaweicloudsdkdis.v2.model.send_records_response import SendRecordsResponse
from huaweicloudsdkdis.v2.model.show_app_request import ShowAppRequest
from huaweicloudsdkdis.v2.model.show_app_response import ShowAppResponse
from huaweicloudsdkdis.v2.model.show_checkpoint_request import ShowCheckpointRequest
from huaweicloudsdkdis.v2.model.show_checkpoint_response import ShowCheckpointResponse
from huaweicloudsdkdis.v2.model.show_consumer_state_request import ShowConsumerStateRequest
from huaweicloudsdkdis.v2.model.show_consumer_state_response import ShowConsumerStateResponse
from huaweicloudsdkdis.v2.model.show_cursor_request import ShowCursorRequest
from huaweicloudsdkdis.v2.model.show_cursor_response import ShowCursorResponse
from huaweicloudsdkdis.v2.model.show_partition_metrics_request import ShowPartitionMetricsRequest
from huaweicloudsdkdis.v2.model.show_partition_metrics_response import ShowPartitionMetricsResponse
from huaweicloudsdkdis.v2.model.show_stream_metrics_request import ShowStreamMetricsRequest
from huaweicloudsdkdis.v2.model.show_stream_metrics_response import ShowStreamMetricsResponse
from huaweicloudsdkdis.v2.model.show_stream_request import ShowStreamRequest
from huaweicloudsdkdis.v2.model.show_stream_response import ShowStreamResponse
from huaweicloudsdkdis.v2.model.show_stream_tags_request import ShowStreamTagsRequest
from huaweicloudsdkdis.v2.model.show_stream_tags_response import ShowStreamTagsResponse
from huaweicloudsdkdis.v2.model.show_transfer_task_request import ShowTransferTaskRequest
from huaweicloudsdkdis.v2.model.show_transfer_task_response import ShowTransferTaskResponse
from huaweicloudsdkdis.v2.model.stream_info import StreamInfo
from huaweicloudsdkdis.v2.model.sys_tag import SysTag
from huaweicloudsdkdis.v2.model.tag import Tag
from huaweicloudsdkdis.v2.model.tags import Tags
from huaweicloudsdkdis.v2.model.transfer_task import TransferTask
from huaweicloudsdkdis.v2.model.update_partition_count import UpdatePartitionCount
from huaweicloudsdkdis.v2.model.update_partition_count_req import UpdatePartitionCountReq
from huaweicloudsdkdis.v2.model.update_partition_count_request import UpdatePartitionCountRequest
from huaweicloudsdkdis.v2.model.update_partition_count_response import UpdatePartitionCountResponse
from huaweicloudsdkdis.v2.model.update_stream_req import UpdateStreamReq
from huaweicloudsdkdis.v2.model.update_stream_request import UpdateStreamRequest
from huaweicloudsdkdis.v2.model.update_stream_response import UpdateStreamResponse


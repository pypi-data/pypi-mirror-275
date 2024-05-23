# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkcloudide.v2.cloudide_client import CloudIDEClient
from huaweicloudsdkcloudide.v2.cloudide_async_client import CloudIDEAsyncClient

from huaweicloudsdkcloudide.v2.model.acceptance_schema import AcceptanceSchema
from huaweicloudsdkcloudide.v2.model.account_status import AccountStatus
from huaweicloudsdkcloudide.v2.model.add_extension_evaluation_reply_request import AddExtensionEvaluationReplyRequest
from huaweicloudsdkcloudide.v2.model.add_extension_evaluation_reply_response import AddExtensionEvaluationReplyResponse
from huaweicloudsdkcloudide.v2.model.add_extension_evaluation_request import AddExtensionEvaluationRequest
from huaweicloudsdkcloudide.v2.model.add_extension_evaluation_response import AddExtensionEvaluationResponse
from huaweicloudsdkcloudide.v2.model.add_extension_star_request import AddExtensionStarRequest
from huaweicloudsdkcloudide.v2.model.add_extension_star_response import AddExtensionStarResponse
from huaweicloudsdkcloudide.v2.model.attributes import Attributes
from huaweicloudsdkcloudide.v2.model.chat_request_message import ChatRequestMessage
from huaweicloudsdkcloudide.v2.model.chat_result_request_message import ChatResultRequestMessage
from huaweicloudsdkcloudide.v2.model.check_instance_access_request import CheckInstanceAccessRequest
from huaweicloudsdkcloudide.v2.model.check_instance_access_response import CheckInstanceAccessResponse
from huaweicloudsdkcloudide.v2.model.check_malicious_extension_evaluation_request import CheckMaliciousExtensionEvaluationRequest
from huaweicloudsdkcloudide.v2.model.check_malicious_extension_evaluation_response import CheckMaliciousExtensionEvaluationResponse
from huaweicloudsdkcloudide.v2.model.check_name_request import CheckNameRequest
from huaweicloudsdkcloudide.v2.model.check_name_response import CheckNameResponse
from huaweicloudsdkcloudide.v2.model.check_result import CheckResult
from huaweicloudsdkcloudide.v2.model.check_result_error import CheckResultError
from huaweicloudsdkcloudide.v2.model.code_arts_ide_online_extension_version_property import CodeArtsIDEOnlineExtensionVersionProperty
from huaweicloudsdkcloudide.v2.model.create_acceptance_request import CreateAcceptanceRequest
from huaweicloudsdkcloudide.v2.model.create_acceptance_response import CreateAcceptanceResponse
from huaweicloudsdkcloudide.v2.model.create_apply_request import CreateApplyRequest
from huaweicloudsdkcloudide.v2.model.create_apply_response import CreateApplyResponse
from huaweicloudsdkcloudide.v2.model.create_event_request import CreateEventRequest
from huaweicloudsdkcloudide.v2.model.create_event_response import CreateEventResponse
from huaweicloudsdkcloudide.v2.model.create_extension_authorization_request import CreateExtensionAuthorizationRequest
from huaweicloudsdkcloudide.v2.model.create_extension_authorization_response import CreateExtensionAuthorizationResponse
from huaweicloudsdkcloudide.v2.model.create_instance_by3rd_request import CreateInstanceBy3rdRequest
from huaweicloudsdkcloudide.v2.model.create_instance_by3rd_response import CreateInstanceBy3rdResponse
from huaweicloudsdkcloudide.v2.model.create_instance_request import CreateInstanceRequest
from huaweicloudsdkcloudide.v2.model.create_instance_response import CreateInstanceResponse
from huaweicloudsdkcloudide.v2.model.create_login_request import CreateLoginRequest
from huaweicloudsdkcloudide.v2.model.create_login_response import CreateLoginResponse
from huaweicloudsdkcloudide.v2.model.create_request_request import CreateRequestRequest
from huaweicloudsdkcloudide.v2.model.create_request_response import CreateRequestResponse
from huaweicloudsdkcloudide.v2.model.criteria_snake import CriteriaSnake
from huaweicloudsdkcloudide.v2.model.delete_evaluation_reply_request import DeleteEvaluationReplyRequest
from huaweicloudsdkcloudide.v2.model.delete_evaluation_reply_response import DeleteEvaluationReplyResponse
from huaweicloudsdkcloudide.v2.model.delete_evaluation_request import DeleteEvaluationRequest
from huaweicloudsdkcloudide.v2.model.delete_evaluation_response import DeleteEvaluationResponse
from huaweicloudsdkcloudide.v2.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkcloudide.v2.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkcloudide.v2.model.error import Error
from huaweicloudsdkcloudide.v2.model.evaluation import Evaluation
from huaweicloudsdkcloudide.v2.model.evaluation_accusation import EvaluationAccusation
from huaweicloudsdkcloudide.v2.model.evaluation_reply import EvaluationReply
from huaweicloudsdkcloudide.v2.model.event_schema import EventSchema
from huaweicloudsdkcloudide.v2.model.expire_vo import ExpireVo
from huaweicloudsdkcloudide.v2.model.extension_all_snake import ExtensionAllSnake
from huaweicloudsdkcloudide.v2.model.extension_authorization import ExtensionAuthorization
from huaweicloudsdkcloudide.v2.model.extension_external_info import ExtensionExternalInfo
from huaweicloudsdkcloudide.v2.model.extension_file_snake import ExtensionFileSnake
from huaweicloudsdkcloudide.v2.model.extension_query_param_snake import ExtensionQueryParamSnake
from huaweicloudsdkcloudide.v2.model.extension_query_result import ExtensionQueryResult
from huaweicloudsdkcloudide.v2.model.extension_search_user_input_param_customize_for_detail import ExtensionSearchUserInputParamCustomizeForDetail
from huaweicloudsdkcloudide.v2.model.extension_star import ExtensionStar
from huaweicloudsdkcloudide.v2.model.extension_statistics import ExtensionStatistics
from huaweicloudsdkcloudide.v2.model.extension_version_snake import ExtensionVersionSnake
from huaweicloudsdkcloudide.v2.model.filter_snake import FilterSnake
from huaweicloudsdkcloudide.v2.model.instance_edge_param import InstanceEdgeParam
from huaweicloudsdkcloudide.v2.model.instance_param import InstanceParam
from huaweicloudsdkcloudide.v2.model.instance_status_response import InstanceStatusResponse
from huaweicloudsdkcloudide.v2.model.instance_update_param import InstanceUpdateParam
from huaweicloudsdkcloudide.v2.model.instances_response_instances_vo_result import InstancesResponseInstancesVOResult
from huaweicloudsdkcloudide.v2.model.instances_vo import InstancesVO
from huaweicloudsdkcloudide.v2.model.join_request_schema import JoinRequestSchema
from huaweicloudsdkcloudide.v2.model.list_extensions_request import ListExtensionsRequest
from huaweicloudsdkcloudide.v2.model.list_extensions_response import ListExtensionsResponse
from huaweicloudsdkcloudide.v2.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkcloudide.v2.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkcloudide.v2.model.list_org_instances_request import ListOrgInstancesRequest
from huaweicloudsdkcloudide.v2.model.list_org_instances_response import ListOrgInstancesResponse
from huaweicloudsdkcloudide.v2.model.list_project_templates_request import ListProjectTemplatesRequest
from huaweicloudsdkcloudide.v2.model.list_project_templates_response import ListProjectTemplatesResponse
from huaweicloudsdkcloudide.v2.model.list_publisher_request import ListPublisherRequest
from huaweicloudsdkcloudide.v2.model.list_publisher_response import ListPublisherResponse
from huaweicloudsdkcloudide.v2.model.list_stacks_request import ListStacksRequest
from huaweicloudsdkcloudide.v2.model.list_stacks_response import ListStacksResponse
from huaweicloudsdkcloudide.v2.model.login_schema import LoginSchema
from huaweicloudsdkcloudide.v2.model.member_role_vo import MemberRoleVo
from huaweicloudsdkcloudide.v2.model.page_instances_vo import PageInstancesVO
from huaweicloudsdkcloudide.v2.model.plugin import Plugin
from huaweicloudsdkcloudide.v2.model.project_templates import ProjectTemplates
from huaweicloudsdkcloudide.v2.model.properties_schema import PropertiesSchema
from huaweicloudsdkcloudide.v2.model.publish_extension_request import PublishExtensionRequest
from huaweicloudsdkcloudide.v2.model.publish_extension_response import PublishExtensionResponse
from huaweicloudsdkcloudide.v2.model.publisher_snake import PublisherSnake
from huaweicloudsdkcloudide.v2.model.publisher_vo import PublisherVO
from huaweicloudsdkcloudide.v2.model.recipe import Recipe
from huaweicloudsdkcloudide.v2.model.request_status import RequestStatus
from huaweicloudsdkcloudide.v2.model.resource_price import ResourcePrice
from huaweicloudsdkcloudide.v2.model.result_metadata_snake import ResultMetadataSnake
from huaweicloudsdkcloudide.v2.model.show_account_status_request import ShowAccountStatusRequest
from huaweicloudsdkcloudide.v2.model.show_account_status_response import ShowAccountStatusResponse
from huaweicloudsdkcloudide.v2.model.show_category_list_request import ShowCategoryListRequest
from huaweicloudsdkcloudide.v2.model.show_category_list_response import ShowCategoryListResponse
from huaweicloudsdkcloudide.v2.model.show_extension_authorization_request import ShowExtensionAuthorizationRequest
from huaweicloudsdkcloudide.v2.model.show_extension_authorization_response import ShowExtensionAuthorizationResponse
from huaweicloudsdkcloudide.v2.model.show_extension_detail_request import ShowExtensionDetailRequest
from huaweicloudsdkcloudide.v2.model.show_extension_detail_response import ShowExtensionDetailResponse
from huaweicloudsdkcloudide.v2.model.show_extension_evaluation_request import ShowExtensionEvaluationRequest
from huaweicloudsdkcloudide.v2.model.show_extension_evaluation_response import ShowExtensionEvaluationResponse
from huaweicloudsdkcloudide.v2.model.show_extension_evaluation_star_request import ShowExtensionEvaluationStarRequest
from huaweicloudsdkcloudide.v2.model.show_extension_evaluation_star_response import ShowExtensionEvaluationStarResponse
from huaweicloudsdkcloudide.v2.model.show_extension_testing_result_request import ShowExtensionTestingResultRequest
from huaweicloudsdkcloudide.v2.model.show_extension_testing_result_response import ShowExtensionTestingResultResponse
from huaweicloudsdkcloudide.v2.model.show_instance_request import ShowInstanceRequest
from huaweicloudsdkcloudide.v2.model.show_instance_response import ShowInstanceResponse
from huaweicloudsdkcloudide.v2.model.show_instance_status_info_request import ShowInstanceStatusInfoRequest
from huaweicloudsdkcloudide.v2.model.show_instance_status_info_response import ShowInstanceStatusInfoResponse
from huaweicloudsdkcloudide.v2.model.show_price_request import ShowPriceRequest
from huaweicloudsdkcloudide.v2.model.show_price_response import ShowPriceResponse
from huaweicloudsdkcloudide.v2.model.show_result_request import ShowResultRequest
from huaweicloudsdkcloudide.v2.model.show_result_response import ShowResultResponse
from huaweicloudsdkcloudide.v2.model.source_storage import SourceStorage
from huaweicloudsdkcloudide.v2.model.stack_info import StackInfo
from huaweicloudsdkcloudide.v2.model.stacks_attribute import StacksAttribute
from huaweicloudsdkcloudide.v2.model.stacks_config import StacksConfig
from huaweicloudsdkcloudide.v2.model.stacks_tags import StacksTags
from huaweicloudsdkcloudide.v2.model.start_chat_request import StartChatRequest
from huaweicloudsdkcloudide.v2.model.start_chat_request_message import StartChatRequestMessage
from huaweicloudsdkcloudide.v2.model.start_chat_response import StartChatResponse
from huaweicloudsdkcloudide.v2.model.start_instance_param import StartInstanceParam
from huaweicloudsdkcloudide.v2.model.start_instance_request import StartInstanceRequest
from huaweicloudsdkcloudide.v2.model.start_instance_response import StartInstanceResponse
from huaweicloudsdkcloudide.v2.model.stop_instance_request import StopInstanceRequest
from huaweicloudsdkcloudide.v2.model.stop_instance_response import StopInstanceResponse
from huaweicloudsdkcloudide.v2.model.sync_chat_request import SyncChatRequest
from huaweicloudsdkcloudide.v2.model.sync_chat_response import SyncChatResponse
from huaweicloudsdkcloudide.v2.model.sync_get_chat_result_request import SyncGetChatResultRequest
from huaweicloudsdkcloudide.v2.model.sync_get_chat_result_response import SyncGetChatResultResponse
from huaweicloudsdkcloudide.v2.model.task_model import TaskModel
from huaweicloudsdkcloudide.v2.model.task_model_market_place import TaskModelMarketPlace
from huaweicloudsdkcloudide.v2.model.update_instance_activity_request import UpdateInstanceActivityRequest
from huaweicloudsdkcloudide.v2.model.update_instance_activity_response import UpdateInstanceActivityResponse
from huaweicloudsdkcloudide.v2.model.update_instance_request import UpdateInstanceRequest
from huaweicloudsdkcloudide.v2.model.update_instance_response import UpdateInstanceResponse
from huaweicloudsdkcloudide.v2.model.upload_extension_file_request import UploadExtensionFileRequest
from huaweicloudsdkcloudide.v2.model.upload_extension_file_request_body import UploadExtensionFileRequestBody
from huaweicloudsdkcloudide.v2.model.upload_extension_file_response import UploadExtensionFileResponse
from huaweicloudsdkcloudide.v2.model.upload_file_publisher_request import UploadFilePublisherRequest
from huaweicloudsdkcloudide.v2.model.upload_file_publisher_request_body import UploadFilePublisherRequestBody
from huaweicloudsdkcloudide.v2.model.upload_file_publisher_response import UploadFilePublisherResponse


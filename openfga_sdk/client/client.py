"""
   Python SDK for OpenFGA

   API version: 1.x
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

import asyncio
import uuid

from openfga_sdk.api.open_fga_api import OpenFgaApi
from openfga_sdk.api_client import ApiClient
from openfga_sdk.client.configuration import ClientConfiguration
from openfga_sdk.client.models.assertion import ClientAssertion
from openfga_sdk.client.models.batch_check_response import BatchCheckResponse
from openfga_sdk.client.models.check_request import (
    ClientCheckRequest,
    construct_check_request,
)
from openfga_sdk.client.models.expand_request import ClientExpandRequest
from openfga_sdk.client.models.list_objects_request import ClientListObjectsRequest
from openfga_sdk.client.models.list_relations_request import ClientListRelationsRequest
from openfga_sdk.client.models.list_users_request import ClientListUsersRequest
from openfga_sdk.client.models.read_changes_request import ClientReadChangesRequest
from openfga_sdk.client.models.tuple import ClientTuple, convert_tuple_keys
from openfga_sdk.client.models.write_request import ClientWriteRequest
from openfga_sdk.client.models.write_response import ClientWriteResponse
from openfga_sdk.client.models.write_single_response import (
    construct_write_single_response,
)
from openfga_sdk.client.models.write_transaction_opts import WriteTransactionOpts
from openfga_sdk.exceptions import (
    AuthenticationError,
    FgaValidationException,
    UnauthorizedException,
)
from openfga_sdk.models.assertion import Assertion
from openfga_sdk.models.check_request import CheckRequest
from openfga_sdk.models.contextual_tuple_keys import ContextualTupleKeys
from openfga_sdk.models.create_store_request import CreateStoreRequest
from openfga_sdk.models.expand_request import ExpandRequest
from openfga_sdk.models.expand_request_tuple_key import ExpandRequestTupleKey
from openfga_sdk.models.list_objects_request import ListObjectsRequest
from openfga_sdk.models.list_users_request import ListUsersRequest
from openfga_sdk.models.read_authorization_model_response import (
    ReadAuthorizationModelResponse,
)
from openfga_sdk.models.read_request import ReadRequest
from openfga_sdk.models.read_request_tuple_key import ReadRequestTupleKey
from openfga_sdk.models.tuple_key import TupleKey
from openfga_sdk.models.write_assertions_request import WriteAssertionsRequest
from openfga_sdk.models.write_authorization_model_request import (
    WriteAuthorizationModelRequest,
)
from openfga_sdk.models.write_request import WriteRequest
from openfga_sdk.validation import is_well_formed_ulid_string

CLIENT_METHOD_HEADER = "X-OpenFGA-Client-Method"
CLIENT_BULK_REQUEST_ID_HEADER = "X-OpenFGA-Client-Bulk-Request-Id"


def _chuck_array(array, max_size):
    """
    Helper function to chuck array into arrays of max_size
    """
    return [
        array[i * max_size : (i + 1) * max_size]
        for i in range((len(array) + max_size - 1) // max_size)
    ]


def set_heading_if_not_set(options: dict[str, int | str], name: str, value: str):
    """
    Set heading to the value if it is not set
    """
    if options is None:
        options = {}
    headers = options.get("headers")
    if headers is None:
        headers = {}
    if headers.get(name) is None:
        headers[name] = value
    options["headers"] = headers
    return options


def options_to_kwargs(options: dict[str, int | str] = None):
    """
    Return kwargs with continuation_token and page_size
    """
    kwargs = {}
    if options is not None:
        if options.get("page_size"):
            kwargs["page_size"] = options["page_size"]
        if options.get("continuation_token"):
            kwargs["continuation_token"] = options["continuation_token"]
        if options.get("headers"):
            kwargs["_headers"] = options["headers"]
        if options.get("retry_params"):
            kwargs["_retry_params"] = options["retry_params"]
    return kwargs


def options_to_transaction_info(options: dict[str, int | str] = None):
    """
    Return the transaction info
    """
    if options is not None and options.get("transaction"):
        return options["transaction"]
    return WriteTransactionOpts()


def _check_allowed(response: BatchCheckResponse):
    """
    Helper function to return whether the response is check is allowed
    """
    return response.allowed


class OpenFgaClient:
    """
    OpenFgaClient is the entry point for invoking calls against the OpenFGA API.
    """

    def __init__(self, configuration: ClientConfiguration):
        self._client_configuration = configuration
        self._api_client = ApiClient(configuration)
        self._api = OpenFgaApi(self._api_client)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def close(self):
        await self._api.close()

    def _get_authorization_model_id(self, options: object) -> str | None:
        """
        Return the authorization model ID if specified in the options.
        Otherwise, return the authorization model ID stored in the client's configuration
        """
        authorization_model_id = self._client_configuration.authorization_model_id
        if options is not None and "authorization_model_id" in options:
            authorization_model_id = options["authorization_model_id"]
        if authorization_model_id is None or authorization_model_id == "":
            return None
        if is_well_formed_ulid_string(authorization_model_id) is False:
            raise FgaValidationException(
                "authorization_model_id ('%s') is not in a valid ulid format"
                % authorization_model_id
            )
        return authorization_model_id

    def set_store_id(self, value):
        """
        Update the store ID in the configuration
        """
        self._api_client.set_store_id(value)

    def get_store_id(self):
        """
        Return the store id (if any) store in the configuration
        """
        return self._api_client.get_store_id()

    def set_authorization_model_id(self, value):
        """
        Update the authorization model id in the configuration
        """
        self._client_configuration.authorization_model_id = value

    def get_authorization_model_id(self):
        """
        Return the authorization model id
        """
        return self._client_configuration.authorization_model_id

    #################
    # Stores
    #################

    async def list_stores(self, options: dict[str, int | str] = None):
        """
        List the stores in the system
        :param page_size(options) - Number of items returned per request
        :param continuation_token(options) - No continuation_token by default
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        # convert options to kwargs
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "ListStores")
        kwargs = options_to_kwargs(options)
        api_response = await self._api.list_stores(
            **kwargs,
        )
        return api_response

    async def create_store(
        self, body: CreateStoreRequest, options: dict[str, int | str] = None
    ):
        """
        Create the stores in the system
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "CreateStore")
        kwargs = options_to_kwargs(options)
        api_response = await self._api.create_store(body, **kwargs)
        return api_response

    async def get_store(self, options: dict[str, int | str] = None):
        """
        Get the store info in the system. Store id is from the configuration.
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "GetStore")
        kwargs = options_to_kwargs(options)
        api_response = await self._api.get_store(
            **kwargs,
        )
        return api_response

    async def delete_store(self, options: dict[str, int | str] = None):
        """
        Delete the store from the system. Store id is from the configuration.
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "DeleteStore")
        kwargs = options_to_kwargs(options)
        api_response = await self._api.delete_store(
            **kwargs,
        )
        return api_response

    #######################
    # Authorization Models
    #######################

    async def read_authorization_models(self, options: dict[str, int | str] = None):
        """
        Return all the authorization models for a particular store.
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(
            options, CLIENT_METHOD_HEADER, "ReadAuthorizationModels"
        )
        kwargs = options_to_kwargs(options)
        api_response = await self._api.read_authorization_models(
            **kwargs,
        )
        return api_response

    async def write_authorization_model(
        self, body: WriteAuthorizationModelRequest, options: dict[str, int | str] = None
    ):
        """
        Write authorization model.
        :param body - WriteAuthorizationModelRequest
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(
            options, CLIENT_METHOD_HEADER, "WriteAuthorizationModel"
        )
        kwargs = options_to_kwargs(options)
        api_response = await self._api.write_authorization_model(
            body,
            **kwargs,
        )
        return api_response

    async def read_authorization_model(self, options: dict[str, int | str] = None):
        """
        Read an authorization model.
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(
            options, CLIENT_METHOD_HEADER, "ReadAuthorizationModel"
        )
        kwargs = options_to_kwargs(options)
        authorization_model_id = self._get_authorization_model_id(options)
        api_response = await self._api.read_authorization_model(
            authorization_model_id,
            **kwargs,
        )
        return api_response

    async def read_latest_authorization_model(
        self, options: dict[str, int | str] = None
    ):
        """
        Convenient method of reading the latest authorization model
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(
            options, CLIENT_METHOD_HEADER, "ReadLatestAuthoriationModel"
        )
        options["page_size"] = 1
        api_response = await self.read_authorization_models(options)
        return ReadAuthorizationModelResponse(api_response.authorization_models[0])

    #######################
    # Relationship Tuples
    #######################

    async def read_changes(
        self, body: ClientReadChangesRequest, options: dict[str, str] = None
    ):
        """
        Read changes for specified type
        :param body - the type we want to look for change
        :param page_size(options) - Number of items returned per request
        :param continuation_token(options) - No continuation_token by default
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "ReadChanges")
        kwargs = options_to_kwargs(options)
        kwargs["type"] = body.type
        api_response = await self._api.read_changes(
            **kwargs,
        )
        return api_response

    async def read(self, body: ReadRequestTupleKey, options: dict[str, str] = None):
        """
        Read changes for specified type
        :param body - the tuples we want to read
        :param page_size(options) - Number of items returned per request
        :param continuation_token(options) - No continuation_token by default
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "Read")
        page_size = None
        continuation_token = None
        if options:
            if options.get("page_size"):
                page_size = options.get("page_size")
                options.pop("page_size")
            if options.get("continuation_token"):
                continuation_token = options.get("continuation_token")
                options.pop("continuation_token")
        kwargs = options_to_kwargs(options)

        if body is None or (
            body.object is None and body.relation is None and body.user is None
        ):
            tuple_key = None
        else:
            tuple_key = body

        api_response = await self._api.read(
            ReadRequest(
                tuple_key=tuple_key,
                page_size=page_size,
                continuation_token=continuation_token,
            ),
            **kwargs,
        )
        return api_response

    async def _write_single_batch(
        self, batch: list[ClientTuple], is_write: bool, options: dict[str, str] = None
    ):
        try:
            write_batch = None
            delete_batch = None
            if is_write:
                write_batch = batch
            else:
                delete_batch = batch
            await self._write_with_transaction(
                ClientWriteRequest(writes=write_batch, deletes=delete_batch), options
            )
            return [construct_write_single_response(i, True, None) for i in batch]
        except (AuthenticationError, UnauthorizedException) as err:
            raise err
        except Exception as err:
            return [construct_write_single_response(i, False, err) for i in batch]

    async def _write_batches(
        self,
        tuple_keys: list[ClientTuple],
        transaction: WriteTransactionOpts,
        is_write: bool,
        options: dict[str, str] = None,
    ):
        """
        Internal function for write/delete batches
        """
        chunks = _chuck_array(tuple_keys, transaction.max_per_chunk)

        write_batches = _chuck_array(chunks, transaction.max_parallel_requests)
        batch_write_responses = []
        for write_batch in write_batches:
            request = [
                self._write_single_batch(i, is_write, options) for i in write_batch
            ]
            response = await asyncio.gather(*request)
            flatten_list = [
                item
                for batch_single_response in response
                for item in batch_single_response
            ]
            batch_write_responses.extend(flatten_list)

        return batch_write_responses

    async def _write_with_transaction(
        self, body: ClientWriteRequest, options: dict[str, str] = None
    ):
        """
        Write or deletes tuples
        """
        kwargs = options_to_kwargs(options)
        writes_tuple_keys = None
        deletes_tuple_keys = None
        if body.writes_tuple_keys:
            writes_tuple_keys = body.writes_tuple_keys
        if body.deletes_tuple_keys:
            deletes_tuple_keys = body.deletes_tuple_keys

        await self._api.write(
            WriteRequest(
                writes=writes_tuple_keys,
                deletes=deletes_tuple_keys,
                authorization_model_id=self._get_authorization_model_id(options),
            ),
            **kwargs,
        )
        # any error will result in exception being thrown and not reached below code
        writes_response = None
        if body.writes:
            writes_response = [
                construct_write_single_response(i, True, None) for i in body.writes
            ]
        deletes_response = None
        if body.deletes:
            deletes_response = [
                construct_write_single_response(i, True, None) for i in body.deletes
            ]
        return ClientWriteResponse(writes=writes_response, deletes=deletes_response)

    async def write(self, body: ClientWriteRequest, options: dict[str, str] = None):
        """
        Write or deletes tuples
        :param body - the write request
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "Writes")
        transaction = options_to_transaction_info(options)
        if not transaction.disabled:
            results = await self._write_with_transaction(body, options)
            return results

        options = set_heading_if_not_set(
            options, CLIENT_BULK_REQUEST_ID_HEADER, str(uuid.uuid4())
        )

        # otherwise, it is not a transaction and it is a batch write requests
        writes_response = None
        if body.writes:
            writes_response = await self._write_batches(
                body.writes, transaction, True, options
            )
        deletes_response = None
        if body.deletes:
            deletes_response = await self._write_batches(
                body.deletes, transaction, False, options
            )
        return ClientWriteResponse(writes=writes_response, deletes=deletes_response)

    async def write_tuples(
        self, body: list[ClientTuple], options: dict[str, str] = None
    ):
        """
        Convenient method for writing tuples
        :param body - the list of tuples we want to write
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "WriteTuples")
        result = await self.write(ClientWriteRequest(body, None), options)
        return result

    async def delete_tuples(
        self, body: list[ClientTuple], options: dict[str, str] = None
    ):
        """
        Convenient method for deleteing tuples
        :param body - the list of tuples we want to delete
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "DeleteTuples")
        result = await self.write(ClientWriteRequest(None, body), options)
        return result

    #######################
    # Relationship Queries
    #######################
    async def check(self, body: ClientCheckRequest, options: dict[str, str] = None):
        """
        Check whether a user is authorized to access an object
        :param body - ClientCheckRequest defining check request
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "Check")

        kwargs = options_to_kwargs(options)

        req_body = CheckRequest(
            tuple_key=TupleKey(
                user=body.user,
                relation=body.relation,
                object=body.object,
            ),
            context=body.context,
            authorization_model_id=self._get_authorization_model_id(options),
        )
        if body.contextual_tuples:
            req_body.contextual_tuples = ContextualTupleKeys(
                tuple_keys=convert_tuple_keys(body.contextual_tuples)
            )
        api_response = await self._api.check(body=req_body, **kwargs)
        return api_response

    async def _single_batch_check(
        self,
        body: ClientCheckRequest,
        semaphore: asyncio.Semaphore,
        options: dict[str, str] = None,
    ):
        """
        Run a single batch request and return body in a SingleBatchCheckResponse
        :param body - ClientCheckRequest defining check request
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        """
        await semaphore.acquire()
        try:
            api_response = await self.check(body, options)
            return BatchCheckResponse(
                allowed=api_response.allowed,
                request=body,
                response=api_response,
                error=None,
            )
        except (AuthenticationError, UnauthorizedException) as err:
            raise err
        except Exception as err:
            return BatchCheckResponse(
                allowed=False, request=body, response=None, error=err
            )
        finally:
            semaphore.release()

    async def batch_check(
        self, body: list[ClientCheckRequest], options: dict[str, str] = None
    ):
        """
        Run a set of checks
        :param body - list of ClientCheckRequest defining check request
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param max_parallel_requests(options) - Max number of requests to issue in parallel. Defaults to 10
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "BatchCheck")
        options = set_heading_if_not_set(
            options, CLIENT_BULK_REQUEST_ID_HEADER, str(uuid.uuid4())
        )

        max_parallel_requests = 10
        if options is not None and "max_parallel_requests" in options:
            max_parallel_requests = options["max_parallel_requests"]

        sem = asyncio.Semaphore(max_parallel_requests)
        batch_check_coros = [
            self._single_batch_check(request, sem, options) for request in body
        ]
        batch_check_response = await asyncio.gather(*batch_check_coros)

        return batch_check_response

    async def expand(self, body: ClientExpandRequest, options: dict[str, str] = None):
        """
        Run expand request
        :param body - list of ClientExpandRequest defining expand request
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "Expand")
        kwargs = options_to_kwargs(options)

        req_body = ExpandRequest(
            tuple_key=ExpandRequestTupleKey(
                relation=body.relation,
                object=body.object,
            ),
            authorization_model_id=self._get_authorization_model_id(options),
        )
        api_response = await self._api.expand(body=req_body, **kwargs)
        return api_response

    async def list_objects(
        self, body: ClientListObjectsRequest, options: dict[str, str] = None
    ):
        """
        Run list object request
        :param body - list object parameters
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "ListObjects")
        kwargs = options_to_kwargs(options)

        req_body = ListObjectsRequest(
            authorization_model_id=self._get_authorization_model_id(options),
            user=body.user,
            relation=body.relation,
            type=body.type,
            context=body.context,
        )
        if body.contextual_tuples:
            req_body.contextual_tuples = ContextualTupleKeys(
                tuple_keys=convert_tuple_keys(body.contextual_tuples)
            )
        api_response = await self._api.list_objects(body=req_body, **kwargs)
        return api_response

    async def list_relations(
        self, body: ClientListRelationsRequest, options: dict[str, str] = None
    ):
        """
        Return all the relations for which user has a relationship with the object
        :param body - list relation request
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "ListRelations")
        options = set_heading_if_not_set(
            options, CLIENT_BULK_REQUEST_ID_HEADER, str(uuid.uuid4())
        )

        request_body = [
            construct_check_request(
                user=body.user,
                relation=i,
                object=body.object,
                contextual_tuples=body.contextual_tuples,
                context=body.context,
            )
            for i in body.relations
        ]
        result = await self.batch_check(request_body, options)
        # need to filter with the allowed response
        result_iterator = filter(_check_allowed, result)
        result_list = list(result_iterator)
        return [i.request.relation for i in result_list]

    async def list_users(
        self, body: ClientListUsersRequest, options: dict[str, str] = None
    ):
        """
        Run list users request
        :param body - list user parameters
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(options, CLIENT_METHOD_HEADER, "ListUsers")
        kwargs = options_to_kwargs(options)

        req_body = ListUsersRequest(
            authorization_model_id=self._get_authorization_model_id(options),
            object=body.object,
            relation=body.relation,
            user_filters=body.user_filters,
            contextual_tuples=body.contextual_tuples,
            context=body.context,
        )

        if body.contextual_tuples:
            req_body.contextual_tuples = ContextualTupleKeys(
                tuple_keys=convert_tuple_keys(body.contextual_tuples)
            )

        api_response = await self._api.list_users(body=req_body, **kwargs)

        return api_response

    #######################
    # Assertions
    #######################
    async def read_assertions(self, options: dict[str, str] = None):
        """
        Return the assertions
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(
            options, CLIENT_METHOD_HEADER, "ReadAssertions"
        )

        kwargs = options_to_kwargs(options)
        authorization_model_id = self._get_authorization_model_id(options)
        api_response = await self._api.read_assertions(authorization_model_id, **kwargs)
        return api_response

    async def write_assertions(
        self, body: list[ClientAssertion], options: dict[str, str] = None
    ):
        """
        Upsert the assertions
        :param body - Write assertion request
        :param authorization_model_id(options) - Overrides the authorization model id in the configuration
        :param header(options) - Custom headers to send alongside the request
        :param retryParams(options) - Override the retry parameters for this request
        :param retryParams.maxRetry(options) - Override the max number of retries on each API request
        :param retryParams.minWaitInMs(options) - Override the minimum wait before a retry is initiated
        """
        options = set_heading_if_not_set(
            options, CLIENT_METHOD_HEADER, "WriteAssertions"
        )
        kwargs = options_to_kwargs(options)
        authorization_model_id = self._get_authorization_model_id(options)

        def map_to_assertion(client_assertion: ClientAssertion):
            return Assertion(
                TupleKey(
                    user=client_assertion.user,
                    relation=client_assertion.relation,
                    object=client_assertion.object,
                ),
                client_assertion.expectation,
            )

        api_request_body = WriteAssertionsRequest(
            [map_to_assertion(client_assertion) for client_assertion in body]
        )
        api_response = await self._api.write_assertions(
            authorization_model_id, api_request_body, **kwargs
        )
        return api_response

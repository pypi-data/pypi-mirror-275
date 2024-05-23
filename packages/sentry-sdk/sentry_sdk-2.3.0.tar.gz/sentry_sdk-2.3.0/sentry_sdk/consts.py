from enum import Enum
from sentry_sdk._types import TYPE_CHECKING

# up top to prevent circular import due to integration import
DEFAULT_MAX_VALUE_LENGTH = 1024


# Also needs to be at the top to prevent circular import
class EndpointType(Enum):
    """
    The type of an endpoint. This is an enum, rather than a constant, for historical reasons
    (the old /store endpoint). The enum also preserve future compatibility, in case we ever
    have a new endpoint.
    """

    ENVELOPE = "envelope"


if TYPE_CHECKING:
    import sentry_sdk

    from typing import Optional
    from typing import Callable
    from typing import Union
    from typing import List
    from typing import Type
    from typing import Dict
    from typing import Any
    from typing import Sequence
    from typing import Tuple
    from typing_extensions import TypedDict

    from sentry_sdk.integrations import Integration

    from sentry_sdk._types import (
        BreadcrumbProcessor,
        Event,
        EventProcessor,
        Hint,
        MeasurementUnit,
        ProfilerMode,
        TracesSampler,
        TransactionProcessor,
        MetricTags,
        MetricValue,
    )

    # Experiments are feature flags to enable and disable certain unstable SDK
    # functionality. Changing them from the defaults (`None`) in production
    # code is highly discouraged. They are not subject to any stability
    # guarantees such as the ones from semantic versioning.
    Experiments = TypedDict(
        "Experiments",
        {
            "attach_explain_plans": dict[str, Any],
            "max_spans": Optional[int],
            "record_sql_params": Optional[bool],
            "otel_powered_performance": Optional[bool],
            "transport_zlib_compression_level": Optional[int],
            "transport_num_pools": Optional[int],
            "enable_metrics": Optional[bool],
            "before_emit_metric": Optional[
                Callable[[str, MetricValue, MeasurementUnit, MetricTags], bool]
            ],
            "metric_code_locations": Optional[bool],
        },
        total=False,
    )

DEFAULT_QUEUE_SIZE = 100
DEFAULT_MAX_BREADCRUMBS = 100
MATCH_ALL = r".*"

FALSE_VALUES = [
    "false",
    "no",
    "off",
    "n",
    "0",
]


class INSTRUMENTER:
    SENTRY = "sentry"
    OTEL = "otel"


class SPANDATA:
    """
    Additional information describing the type of the span.
    See: https://develop.sentry.dev/sdk/performance/span-data-conventions/
    """

    AI_FREQUENCY_PENALTY = "ai.frequency_penalty"
    """
    Used to reduce repetitiveness of generated tokens.
    Example: 0.5
    """

    AI_PRESENCE_PENALTY = "ai.presence_penalty"
    """
    Used to reduce repetitiveness of generated tokens.
    Example: 0.5
    """

    AI_INPUT_MESSAGES = "ai.input_messages"
    """
    The input messages to an LLM call.
    Example: [{"role": "user", "message": "hello"}]
    """

    AI_MODEL_ID = "ai.model_id"
    """
    The unique descriptor of the model being execugted
    Example: gpt-4
    """

    AI_METADATA = "ai.metadata"
    """
    Extra metadata passed to an AI pipeline step.
    Example: {"executed_function": "add_integers"}
    """

    AI_TAGS = "ai.tags"
    """
    Tags that describe an AI pipeline step.
    Example: {"executed_function": "add_integers"}
    """

    AI_STREAMING = "ai.streaming"
    """
    Whether or not the AI model call's repsonse was streamed back asynchronously
    Example: true
    """

    AI_TEMPERATURE = "ai.temperature"
    """
    For an AI model call, the temperature parameter. Temperature essentially means how random the output will be.
    Example: 0.5
    """

    AI_TOP_P = "ai.top_p"
    """
    For an AI model call, the top_p parameter. Top_p essentially controls how random the output will be.
    Example: 0.5
    """

    AI_TOP_K = "ai.top_k"
    """
    For an AI model call, the top_k parameter. Top_k essentially controls how random the output will be.
    Example: 35
    """

    AI_FUNCTION_CALL = "ai.function_call"
    """
    For an AI model call, the function that was called. This is deprecated for OpenAI, and replaced by tool_calls
    """

    AI_TOOL_CALLS = "ai.tool_calls"
    """
    For an AI model call, the function that was called. This is deprecated for OpenAI, and replaced by tool_calls
    """

    AI_TOOLS = "ai.tools"
    """
    For an AI model call, the functions that are available
    """

    AI_RESPONSE_FORMAT = "ai.response_format"
    """
    For an AI model call, the format of the response
    """

    AI_LOGIT_BIAS = "ai.response_format"
    """
    For an AI model call, the logit bias
    """

    AI_PREAMBLE = "ai.preamble"
    """
    For an AI model call, the preamble parameter.
    Preambles are a part of the prompt used to adjust the model's overall behavior and conversation style.
    Example: "You are now a clown."
    """

    AI_RAW_PROMPTING = "ai.raw_prompting"
    """
    Minimize pre-processing done to the prompt sent to the LLM.
    Example: true
    """

    AI_RESPONSES = "ai.responses"
    """
    The responses to an AI model call. Always as a list.
    Example: ["hello", "world"]
    """

    AI_SEED = "ai.seed"
    """
    The seed, ideally models given the same seed and same other parameters will produce the exact same output.
    Example: 123.45
    """

    DB_NAME = "db.name"
    """
    The name of the database being accessed. For commands that switch the database, this should be set to the target database (even if the command fails).
    Example: myDatabase
    """

    DB_USER = "db.user"
    """
    The name of the database user used for connecting to the database.
    See: https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/semantic_conventions/database.md
    Example: my_user
    """

    DB_OPERATION = "db.operation"
    """
    The name of the operation being executed, e.g. the MongoDB command name such as findAndModify, or the SQL keyword.
    See: https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/semantic_conventions/database.md
    Example: findAndModify, HMSET, SELECT
    """

    DB_SYSTEM = "db.system"
    """
    An identifier for the database management system (DBMS) product being used.
    See: https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/semantic_conventions/database.md
    Example: postgresql
    """

    CACHE_HIT = "cache.hit"
    """
    A boolean indicating whether the requested data was found in the cache.
    Example: true
    """

    CACHE_ITEM_SIZE = "cache.item_size"
    """
    The size of the requested data in bytes.
    Example: 58
    """

    CACHE_KEY = "cache.key"
    """
    The key of the requested data.
    Example: template.cache.some_item.867da7e2af8e6b2f3aa7213a4080edb3
    """

    NETWORK_PEER_ADDRESS = "network.peer.address"
    """
    Peer address of the network connection - IP address or Unix domain socket name.
    Example: 10.1.2.80, /tmp/my.sock, localhost
    """

    NETWORK_PEER_PORT = "network.peer.port"
    """
    Peer port number of the network connection.
    Example: 6379
    """

    HTTP_QUERY = "http.query"
    """
    The Query string present in the URL.
    Example: ?foo=bar&bar=baz
    """

    HTTP_FRAGMENT = "http.fragment"
    """
    The Fragments present in the URL.
    Example: #foo=bar
    """

    HTTP_METHOD = "http.method"
    """
    The HTTP method used.
    Example: GET
    """

    HTTP_STATUS_CODE = "http.response.status_code"
    """
    The HTTP status code as an integer.
    Example: 418
    """

    MESSAGING_DESTINATION_NAME = "messaging.destination.name"
    """
    The destination name where the message is being consumed from,
    e.g. the queue name or topic.
    """

    MESSAGING_MESSAGE_ID = "messaging.message.id"
    """
    The message's identifier.
    """

    MESSAGING_MESSAGE_RETRY_COUNT = "messaging.message.retry.count"
    """
    Number of retries/attempts to process a message.
    """

    MESSAGING_SYSTEM = "messaging.system"
    """
    The messaging system's name, e.g. `kafka`, `aws_sqs`
    """

    SERVER_ADDRESS = "server.address"
    """
    Name of the database host.
    Example: example.com
    """

    SERVER_PORT = "server.port"
    """
    Logical server port number
    Example: 80; 8080; 443
    """

    SERVER_SOCKET_ADDRESS = "server.socket.address"
    """
    Physical server IP address or Unix socket address.
    Example: 10.5.3.2
    """

    SERVER_SOCKET_PORT = "server.socket.port"
    """
    Physical server port.
    Recommended: If different than server.port.
    Example: 16456
    """

    CODE_FILEPATH = "code.filepath"
    """
    The source code file name that identifies the code unit as uniquely as possible (preferably an absolute file path).
    Example: "/app/myapplication/http/handler/server.py"
    """

    CODE_LINENO = "code.lineno"
    """
    The line number in `code.filepath` best representing the operation. It SHOULD point within the code unit named in `code.function`.
    Example: 42
    """

    CODE_FUNCTION = "code.function"
    """
    The method or function name, or equivalent (usually rightmost part of the code unit's name).
    Example: "server_request"
    """

    CODE_NAMESPACE = "code.namespace"
    """
    The "namespace" within which `code.function` is defined. Usually the qualified class or module name, such that `code.namespace` + some separator + `code.function` form a unique identifier for the code unit.
    Example: "http.handler"
    """

    THREAD_ID = "thread.id"
    """
    Identifier of a thread from where the span originated. This should be a string.
    Example: "7972576320"
    """

    THREAD_NAME = "thread.name"
    """
    Label identifying a thread from where the span originated. This should be a string.
    Example: "MainThread"
    """


class OP:
    ANTHROPIC_MESSAGES_CREATE = "ai.messages.create.anthropic"
    CACHE_GET = "cache.get"
    CACHE_PUT = "cache.put"
    COHERE_CHAT_COMPLETIONS_CREATE = "ai.chat_completions.create.cohere"
    COHERE_EMBEDDINGS_CREATE = "ai.embeddings.create.cohere"
    DB = "db"
    DB_REDIS = "db.redis"
    EVENT_DJANGO = "event.django"
    FUNCTION = "function"
    FUNCTION_AWS = "function.aws"
    FUNCTION_GCP = "function.gcp"
    GRAPHQL_EXECUTE = "graphql.execute"
    GRAPHQL_MUTATION = "graphql.mutation"
    GRAPHQL_PARSE = "graphql.parse"
    GRAPHQL_RESOLVE = "graphql.resolve"
    GRAPHQL_SUBSCRIPTION = "graphql.subscription"
    GRAPHQL_QUERY = "graphql.query"
    GRAPHQL_VALIDATE = "graphql.validate"
    GRPC_CLIENT = "grpc.client"
    GRPC_SERVER = "grpc.server"
    HTTP_CLIENT = "http.client"
    HTTP_CLIENT_STREAM = "http.client.stream"
    HTTP_SERVER = "http.server"
    MIDDLEWARE_DJANGO = "middleware.django"
    MIDDLEWARE_STARLETTE = "middleware.starlette"
    MIDDLEWARE_STARLETTE_RECEIVE = "middleware.starlette.receive"
    MIDDLEWARE_STARLETTE_SEND = "middleware.starlette.send"
    MIDDLEWARE_STARLITE = "middleware.starlite"
    MIDDLEWARE_STARLITE_RECEIVE = "middleware.starlite.receive"
    MIDDLEWARE_STARLITE_SEND = "middleware.starlite.send"
    OPENAI_CHAT_COMPLETIONS_CREATE = "ai.chat_completions.create.openai"
    OPENAI_EMBEDDINGS_CREATE = "ai.embeddings.create.openai"
    HUGGINGFACE_HUB_CHAT_COMPLETIONS_CREATE = (
        "ai.chat_completions.create.huggingface_hub"
    )
    LANGCHAIN_PIPELINE = "ai.pipeline.langchain"
    LANGCHAIN_RUN = "ai.run.langchain"
    LANGCHAIN_TOOL = "ai.tool.langchain"
    LANGCHAIN_AGENT = "ai.agent.langchain"
    LANGCHAIN_CHAT_COMPLETIONS_CREATE = "ai.chat_completions.create.langchain"
    QUEUE_PROCESS = "queue.process"
    QUEUE_PUBLISH = "queue.publish"
    QUEUE_SUBMIT_ARQ = "queue.submit.arq"
    QUEUE_TASK_ARQ = "queue.task.arq"
    QUEUE_SUBMIT_CELERY = "queue.submit.celery"
    QUEUE_TASK_CELERY = "queue.task.celery"
    QUEUE_TASK_RQ = "queue.task.rq"
    QUEUE_SUBMIT_HUEY = "queue.submit.huey"
    QUEUE_TASK_HUEY = "queue.task.huey"
    SUBPROCESS = "subprocess"
    SUBPROCESS_WAIT = "subprocess.wait"
    SUBPROCESS_COMMUNICATE = "subprocess.communicate"
    TEMPLATE_RENDER = "template.render"
    VIEW_RENDER = "view.render"
    VIEW_RESPONSE_RENDER = "view.response.render"
    WEBSOCKET_SERVER = "websocket.server"
    SOCKET_CONNECTION = "socket.connection"
    SOCKET_DNS = "socket.dns"


# This type exists to trick mypy and PyCharm into thinking `init` and `Client`
# take these arguments (even though they take opaque **kwargs)
class ClientConstructor:
    def __init__(
        self,
        dsn=None,  # type: Optional[str]
        max_breadcrumbs=DEFAULT_MAX_BREADCRUMBS,  # type: int
        release=None,  # type: Optional[str]
        environment=None,  # type: Optional[str]
        server_name=None,  # type: Optional[str]
        shutdown_timeout=2,  # type: float
        integrations=[],  # type: Sequence[Integration]  # noqa: B006
        in_app_include=[],  # type: List[str]  # noqa: B006
        in_app_exclude=[],  # type: List[str]  # noqa: B006
        default_integrations=True,  # type: bool
        dist=None,  # type: Optional[str]
        transport=None,  # type: Optional[Union[sentry_sdk.transport.Transport, Type[sentry_sdk.transport.Transport], Callable[[Event], None]]]
        transport_queue_size=DEFAULT_QUEUE_SIZE,  # type: int
        sample_rate=1.0,  # type: float
        send_default_pii=False,  # type: bool
        http_proxy=None,  # type: Optional[str]
        https_proxy=None,  # type: Optional[str]
        ignore_errors=[],  # type: Sequence[Union[type, str]]  # noqa: B006
        max_request_body_size="medium",  # type: str
        socket_options=None,  # type: Optional[List[Tuple[int, int, int | bytes]]]
        keep_alive=False,  # type: bool
        before_send=None,  # type: Optional[EventProcessor]
        before_breadcrumb=None,  # type: Optional[BreadcrumbProcessor]
        debug=None,  # type: Optional[bool]
        attach_stacktrace=False,  # type: bool
        ca_certs=None,  # type: Optional[str]
        propagate_traces=True,  # type: bool
        traces_sample_rate=None,  # type: Optional[float]
        traces_sampler=None,  # type: Optional[TracesSampler]
        profiles_sample_rate=None,  # type: Optional[float]
        profiles_sampler=None,  # type: Optional[TracesSampler]
        profiler_mode=None,  # type: Optional[ProfilerMode]
        auto_enabling_integrations=True,  # type: bool
        auto_session_tracking=True,  # type: bool
        send_client_reports=True,  # type: bool
        _experiments={},  # type: Experiments  # noqa: B006
        proxy_headers=None,  # type: Optional[Dict[str, str]]
        instrumenter=INSTRUMENTER.SENTRY,  # type: Optional[str]
        before_send_transaction=None,  # type: Optional[TransactionProcessor]
        project_root=None,  # type: Optional[str]
        enable_tracing=None,  # type: Optional[bool]
        include_local_variables=True,  # type: Optional[bool]
        include_source_context=True,  # type: Optional[bool]
        trace_propagation_targets=[  # noqa: B006
            MATCH_ALL
        ],  # type: Optional[Sequence[str]]
        functions_to_trace=[],  # type: Sequence[Dict[str, str]]  # noqa: B006
        event_scrubber=None,  # type: Optional[sentry_sdk.scrubber.EventScrubber]
        max_value_length=DEFAULT_MAX_VALUE_LENGTH,  # type: int
        enable_backpressure_handling=True,  # type: bool
        error_sampler=None,  # type: Optional[Callable[[Event, Hint], Union[float, bool]]]
        enable_db_query_source=True,  # type: bool
        db_query_source_threshold_ms=100,  # type: int
        spotlight=None,  # type: Optional[Union[bool, str]]
    ):
        # type: (...) -> None
        pass


def _get_default_options():
    # type: () -> Dict[str, Any]
    import inspect

    if hasattr(inspect, "getfullargspec"):
        getargspec = inspect.getfullargspec
    else:
        getargspec = inspect.getargspec  # type: ignore

    a = getargspec(ClientConstructor.__init__)
    defaults = a.defaults or ()
    return dict(zip(a.args[-len(defaults) :], defaults))


DEFAULT_OPTIONS = _get_default_options()
del _get_default_options


VERSION = "2.3.0"

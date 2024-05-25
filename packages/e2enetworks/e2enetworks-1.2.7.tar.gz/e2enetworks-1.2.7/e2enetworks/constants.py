import os

BASE_URL_MODEL_API_CLIENT = os.environ.get("MODEL_API_CLIENT_HOST", "https://infer.e2enetworks.net/")
MY_ACCOUNT_LB_URL = os.environ.get("E2E_TIR_API_HOST", "https://api.e2enetworks.com/myaccount/")

GPU_URL = "api/v1/gpu/"
BASE_GPU_URL = f"{MY_ACCOUNT_LB_URL}{GPU_URL}"
VALIDATED_SUCCESSFULLY = "Validated Successfully"
INVALID_CREDENTIALS = "Validation Failed, Invalid APIkey or Token"
headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://thor-gpu.e2enetworks.net',
    'Referer': 'https://thor-gpu.e2enetworks.net/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}
MANAGED_STORAGE = "managed"
E2E_OBJECT_STORAGE = "e2e_s3"
BUCKET_TYPES = [MANAGED_STORAGE, E2E_OBJECT_STORAGE]
BUCKET_TYPES_HELP = {
    MANAGED_STORAGE: "To Create New Bucket",
    E2E_OBJECT_STORAGE: " To Use Existing Bucket"
}
NOTEBOOK = "notebook"
INFERENCE = "inference_service"
PIPELINE = "pipeline"

PRIVATE = "private"
CUSTOM = "custom"
REGISTRY = "registry.e2enetworks.net"
FREE_USAGE = "free_usage"
PAID_USAGE = "paid_usage"
INSTANCE_TYPE = [FREE_USAGE, PAID_USAGE]
TRITON = "triton"
TENSORRT = "tensorrt"
PYTORCH = "pytorch"
MODEL_TYPES = ['pytorch', 'triton', 'custom']
S3_ENDPOINT = "objectstore.e2enetworks.net"

WHISPER_DATA_LIMIT_BYTES = 50000000
WHISPER_LARGE_V3 = "whisper-large-v3"
LLAMA_2_13B_CHAT = "llama-2-13b-chat"
STABLE_DIFFUSION_2_1 = "stable-diffusion-2-1"
MIXTRAL_8X7B_INSTRUCT = "mixtral-8x7b-instruct"
CODELLAMA_13B_INSTRUCT = "codellama-13b-instruct"
E5_MISTRAL_7B_INSTRUCT = "e5-mistral-7b-instruct"
AUTO_RENEW_STATUS = 'auto_renew'
AUTO_TERMINATE_STATUS = 'auto_terminate'
CONVERT_TO_HOURLY_BILLING = 'convert_to_hourly_billing'
LLAMA_3_8B_INSTRUCT = "llama-3-8b-instruct"
LLMA = "llma"
STABLE_DIFFUSION = "stable_diffusion"
MPT = "mpt"
CODE_LLAMA = "codellama"
FINETUNED = "finetuned"
MIXTRAL8X7B = 'mixtral8x7b'
MIXTRAL7B = 'mixtral7b'
MIXTRAL7B_INSTRUCT = "mistral-7b-instruct"
MIXTRAL8X7B_INSTRUCT = "mixtral-8x7b-instruct"
GEMMA_7B_IT = "gemma-7b-it"
GEMMA_7B = "gemma-7b"
GEMMA_2B = "gemma-2b"
GEMMA_2B_IT = "gemma-2b-it"
PHI_3_MINI_128K_INSTRUCT = "Phi-3-mini-128k-instruct"
STARCODER2_7B = "starcoder2-7b"
VLLM = "vllm"
TIR_CUSTOM_FRAMEWORKS = [LLMA, STABLE_DIFFUSION, MPT, CODE_LLAMA, MIXTRAL7B, MIXTRAL8X7B, MIXTRAL7B_INSTRUCT, MIXTRAL8X7B_INSTRUCT, GEMMA_7B_IT, GEMMA_7B, GEMMA_2B, GEMMA_2B_IT, TENSORRT, PYTORCH, TRITON, LLAMA_3_8B_INSTRUCT, VLLM, STARCODER2_7B, PHI_3_MINI_128K_INSTRUCT]

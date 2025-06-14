import os
import sys

import configargparse

root_dir = os.path.dirname(os.path.abspath(__file__))
env = os.getenv('ENVIRONMENT', 'local')
default_config_files = "{0}/{1}".format(root_dir, f"default.{env}.yaml")
print(default_config_files)

parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser,
                                  default_config_files=[default_config_files],
                                  auto_env_var_prefix="")
parser.add('--payments_main_url', help='payments_main_url')
parser.add('--consumer_type', help='consumer_type')
parser.add('--env', help='env')
parser.add('--port', help='port')
parser.add('--host', help='host')
parser.add('--mode', help='mode')
parser.add('--server_type', help='server_type')
parser.add('--realm', help='realm')
# debug flag
parser.add('--debug', help='debug', action="store_true")
parser.add('--db_url', help='db_url')

parser.add('--azure_openai_key', help='azure_openai_key')
parser.add('--azure_openai_endpoint', help='azure_openai_endpoint')
parser.add('--azure_deployment_engine', help='azure_deployment_engine')
parser.add('--openai_api_version', help='openai_api_version')

parser.add('--azure_openai_gpt3516k_key', help='azure_openai_gpt3516k_key')
parser.add('--azure_openai_gpt3516k_endpoint', help='azure_openai_gpt3516k_endpoint')
parser.add('--azure_openai_gpt3516k_deployment_name', help='azure_openai_gpt3516k_deployment_name')
parser.add('--azure_openai_gpt3516k_api_version', help='azure_openai_gpt3516k_api_version')

parser.add('--azure_openai_gpt4_key', help='azure_openai_gpt4_key')
parser.add('--azure_openai_gpt4_endpoint', help='azure_openai_gpt4_endpoint')
parser.add('--azure_openai_gpt4_deployment_name', help='azure_openai_gpt4_deployment_name')
parser.add('--azure_openai_gpt4_api_version', help='azure_openai_gpt4_api_version')

parser.add('--azure_openai_gpt4o_mini_key', help='azure_openai_gpt4o_mini_key')
parser.add('--azure_openai_gpt4o_mini_endpoint', help='azure_openai_gpt4o_mini_endpoint')
parser.add('--azure_openai_gpt4o_mini_deployment_name', help='azure_openai_gpt4o_mini_deployment_name')
parser.add('--azure_openai_gpt4o_mini_api_version', help='azure_openai_gpt4o_mini_api_version')

parser.add('--openai_gpt4_key', help='openai_gpt4_key')
parser.add('--claude_35sonnet_key', help='claude_35sonnet_key')
parser.add('--storage_file_assets_private', help='storage_file_assets_private')

parser.add('--azure_devops_fex_reviewer_id', help='azure_devops_fex_reviewer_id')
parser.add('--azure_devops_pat', help='azure_devops_pat')
parser.add('--azure_devops_org_url', help='azure_devops_org_url')
parser.add('--azure_devops_username', help='azure_devops_username')
parser.add('--repo_clone_dir', help='repo_clone_dir')

parser.add('--serp_api_key', help='serp_api_key')
parser.add('--ydc_api_key', help='ydc_api_key')
parser.add('--redis_payments_url', help='redis_payments_url')

# prometheus flag
parser.add('--prometheus', help='prometheus', action="store_true")

parser.add('--K8S_NODE_NAME', help='K8S_NODE_NAME')
parser.add('--K8S_POD_NAMESPACE', help='K8S_POD_NAMESPACE')
parser.add('--K8S_POD_NAME', help='K8S_POD_NAME')

parser.add('--sentry_dsn', help='SENTRY_DSN')
parser.add('--sentry_environment', help='SENTRY_ENVIRONMENT')

parser.add('--google_app_id', help='GOOGLE_APP_ID')
parser.add('--google_app_secret', help='GOOGLE_APP_SECRET')

parser.add('--kafka_broker_list', help='KAFKA_BROKER_LIST')

# external API keys
parser.add('--bing_search_api_key', help='bing_search_api_key')
parser.add('--bing_search_endpoint', help='bing_search_endpoint')

parser.add('--razorpay_api_key', help='razorpay_api_key')
parser.add('--razorpay_api_secret', help='razorpay_api_secret')
parser.add('--razorpay_api_base_url', help='razorpay_api_base_url')
parser.add('--pro_trial_expiration_time_seconds', help='pro_trial_expiration_time_seconds')
parser.add('--clerk_secret_key', help='clerk_secret_key')

parser.add('--paddle_api_secret', help='paddle_api_secret')
parser.add('--paddle_client_token', help='paddle_client_token')
parser.add('--paddle_api_base_url', help='paddle_api_base_url')
parser.add('--fallback_plan_id', help='fallback_plan_id')
parser.add('--subscription_cancellation_at', help='subscription_cancellation_at')

arguments = sys.argv
print(arguments)
argument_options = parser.parse_known_args(arguments)
# print("argument values")
print(parser.format_values())
docker_args = argument_options[0]

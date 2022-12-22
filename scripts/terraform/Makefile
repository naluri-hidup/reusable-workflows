ifeq ($(DESTROY),true)
	DESTROY_FLAG = -destroy
endif

.EXPORT_ALL_VARIABLES:

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# TF_LOG=TRACE
TERRAFORM_BACKEND_BUCKET=naluri-terraform-state
TERRAFORM_BACKEND_REGION=ap-southeast-1
TERRAFORM_BACKEND_ROLE_ARN=arn:aws:iam::502605353565:role/TerraformRole
TERRAFORM_BACKEND_DYNAMODB_TABLE=naluri-terraform-state-lock

TERRAFORM_WORKSPACE=$(TERRAFORM_MODULE)_$(CONFIG_NAME)
TERRAFORM_BACKEND_KEY=$(TERRAFORM_MODULE)/$(CONFIG_NAME)
TERRAFORM_VAR_FILE=$(ROOT_DIR)/config/$(CONFIG_NAME).tfvars
TERRAFORM_FOLDER=terraform

terraform.init:
	terraform -chdir=$(TERRAFORM_FOLDER) init -reconfigure -input=false -upgrade=true \
	-backend-config="key=$(TERRAFORM_BACKEND_KEY)" \
	-backend-config="bucket=$(TERRAFORM_BACKEND_BUCKET)" \
	-backend-config="region=$(TERRAFORM_BACKEND_REGION)" \
	-backend-config="encrypt=true" \
	-backend-config="dynamodb_table=$(TERRAFORM_BACKEND_DYNAMODB_TABLE)" \
	-backend-config="role_arn=$(TERRAFORM_BACKEND_ROLE_ARN)"
	terraform workspace select $(TERRAFORM_WORKSPACE) || terraform workspace new $(TERRAFORM_WORKSPACE)

terraform.plan:
	terraform -chdir=$(TERRAFORM_FOLDER) plan -input=false $(DESTROY_FLAG) -var-file=$(TERRAFORM_VAR_FILE) -out terraform.tfplan

terraform.apply:
	terraform -chdir=$(TERRAFORM_FOLDER) apply -input=false -auto-approve terraform.tfplan

terraform.state pull:
	terraform -chdir=$(TERRAFORM_FOLDER) state pull | jq '.resources[] | select(.type == "aws_iam_access_key") | .instances[0].attributes'

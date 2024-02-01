# Some common AWS CLI commands

- To create a stack in AWS cli:

```bash
aws cloudformation create-stack --stack-name AkwasiAutoScalingStack  --template-body file://autoscaling-group.iac.yaml | cat

aws cloudformation describe-stacks

aws cloudformation delete-stack --stack-name AkwasiAutoScalingStack | cat
 ```

# Docker Common Errors

## ImagePullBackOff
Occurs when:
- Image does not exist
- Authentication to registry failed
- Network issues

For AWS ECR:
- EC2 must have permission: ecr:GetAuthorizationToken
- Docker must login using aws ecr get-login-password

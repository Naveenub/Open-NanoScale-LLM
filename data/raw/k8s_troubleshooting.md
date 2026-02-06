# Kubernetes Pod Failures

CrashLoopBackOff indicates:
- Application crash
- Missing environment variables
- Invalid command or entrypoint

Always check:
kubectl logs <pod>
kubectl describe pod <pod>

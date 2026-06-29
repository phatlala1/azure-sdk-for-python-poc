from pathlib import Path

login_seen = Path("mock_azure_login_done.txt").exists()
marker = Path("msrc_azureml_pr_code_after_login.txt")
marker.write_text(
    "poc_marker=azureml_pr_controlled_promptflow_ci_ran_after_mock_login\n"
    f"mock_azure_login_seen_by_pr_code={str(login_seen).lower()}\n"
    "source=scripts/promptflow-ci/promptflow_ci.py\n",
    encoding="utf-8",
)

print("poc_phase=promptflow_ci")
print(f"mock_azure_login_seen_by_pr_code={str(login_seen).lower()}")

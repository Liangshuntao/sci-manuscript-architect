$ErrorActionPreference = "Stop"

$repo = "E:\GPT\sci-manuscript-architect-github"
$logDir = Join-Path $repo ".sync-logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logPath = Join-Path $logDir "weekly_sync_$timestamp.log"

Start-Transcript -Path $logPath -Append | Out-Null
try {
    if (-not (Test-Path (Join-Path $repo ".git"))) {
        throw "Git repository not found: $repo"
    }

    git -C $repo add -A
    git -C $repo diff --cached --quiet

    if ($LASTEXITCODE -eq 0) {
        Write-Output "No staged changes to sync."
        exit 0
    }

    $messageTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git -C $repo commit -m "auto sync sci-manuscript-architect $messageTime"
    git -C $repo push origin main
}
finally {
    Stop-Transcript | Out-Null
}

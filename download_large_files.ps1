# download_large_files.ps1
$torchCpuUrl = "https://drive.google.com/file/d/1zEgeeb6u0kh5iVuIH4veVnsIYqbz7ivf/view?usp=drive_link"
$dnnlLibUrl = "https://drive.google.com/file/d/1VRBDD6KV9mhIVxq15M2_atnLWYccp5SL/view?usp=drive_link"
$torchCpuPath = "venv/Lib/site-packages/torch/lib/torch_cpu.dll"
$dnnlLibPath = "venv/Lib/site-packages/torch/lib/dnnl.lib"

Invoke-WebRequest -Uri $torchCpuUrl -OutFile $torchCpuPath
Invoke-WebRequest -Uri $dnnlLibUrl -OutFile $dnnlLibPath

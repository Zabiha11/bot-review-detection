import subprocess
import sys

scripts = [

    "src.data_pipeline.load_data",

    "src.preprocessing.clean_reviews",

    "src.preprocessing.split_data",

    "src.graph.build_graph_tables"
]

for script in scripts:

    print(f"\n🚀 Running: {script}")

    subprocess.run([
        sys.executable,
        "-m",
        script
    ])

print("\n✅ Phase 1 Pipeline Complete")
import os

# Paths
archive_directory_cluster = os.path.join(os.sep, "W:", os.sep, "wren_archive", "nextseq")
results_directory_cluster = os.path.join(os.sep, "W:", os.sep, "wren_results")
results_directory_l_drive = os.path.join(os.sep, "L:", os.sep, "NGS ANALYSIS", "TruSightCancer")

'''TEST DIRECTORY STRUCTURE
archive_directory_cluster = os.path.join("tests", "raw")
results_directory_cluster = os.path.join("tests")
results_directory_l_drive = os.path.join("tests", "output")
'''

sample_directories = []
sample_files = ["gene_coverage_summary.csv", "gaps_20x.csv"]
cnv_files = ["cnv_report.csv"]
cnv_failure = ["Failures.txt"]

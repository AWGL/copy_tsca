import os

# Paths
archive_directory_cluster = os.path.join(os.sep, "T:", os.sep, "nextseq")
results_directory_cluster = os.path.join(os.sep, "U:", os.sep)
results_directory_l_drive = os.path.join(os.sep, "L:", os.sep, "NGS ANALYSIS", "TruSightCancer")

'''TEST DIRECTORY STRUCTURE
archive_directory_cluster = os.path.join("tests", "raw")
results_directory_cluster = os.path.join("tests")
results_directory_l_drive = os.path.join("tests", "output")
'''

ntc_names = ["NTC"]
ntc_directories = ["InterOp"]
ntc_files = ["RunInfo.xml", "RunParameters.xml"]
sample_directories = []
sample_files = ["gene_coverage_summary.csv", "gaps_20x.csv"]
cnv_files = ["cnv_report.csv"]

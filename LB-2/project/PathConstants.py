class PathConstants:

    prj_dir = "/home/urfin/Education/LB-2/project/"

    # paths for blind set
    plastp_tab = prj_dir + "data_preparation/hits.blast.tab"
    blind_pdb_dir = prj_dir + "data_preparation/pdb_files/"
    blind_dssp_dir = prj_dir + "data_preparation/dssp_files/"
    blind_dssp_short_dir = prj_dir + "data_preparation/dssp_short/"
    final_blind_data = prj_dir + "data_preparation/final_blind_data.txt"
    filtered_blind_data = prj_dir + "data_preparation/filtered_blind_data.txt"
    clustered_data = prj_dir + "data_preparation/clustered.txt"
    blind_data = prj_dir + "data_preparation/blind_data.txt"
    pdb_files = prj_dir + "data_preparation/pdb_files/"

    # paths for training
    training_dssp_dir = prj_dir + "dssp/"
    training_fasta_dir = prj_dir + "fasta/"

    # paths for pssm
    profiling_dir = prj_dir + "profiling/"
    profiling_uniprot_sprot = profiling_dir + "uniprot_sprot.fasta"
    profiling_pssm = profiling_dir + "pssm/"
    profiling_alns = profiling_dir + "alns/"

    # cross validation dir
    cross_validation_dir = prj_dir + "cv/"

    # dump files
    dump_file = prj_dir + "gor_profile.dump"
    dump_list_of_pdb_ids = prj_dir + "list_of_pdb_ids.dump"
    dump_svm_profile_template = prj_dir + "svm_profile_{}.dump"
    dump_svm_model_template = prj_dir + "svm_model_{}.dump"

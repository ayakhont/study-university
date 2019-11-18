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
    blind_fasta_dir = prj_dir + "data_preparation/fasta_files/"

    # paths for training
    training_dssp_dir = prj_dir + "dssp/"
    training_fasta_dir = prj_dir + "fasta/"

    # paths for pssm
    profiling_dir = prj_dir + "profiling/"
    profiling_uniprot_sprot = profiling_dir + "uniprot_sprot.fasta"
    profiling_pssm = profiling_dir + "pssm/"
    profiling_alns = profiling_dir + "alns/"
    profiling_pssm_blind = profiling_dir + "pssm.blind/"
    profiling_alns_blind = profiling_dir + "alns.blind/"

    # cross validation dir
    cross_validation_dir = prj_dir + "cv/"

    # dump files
    dump_gor_profile_template = profiling_dir + "gor_profile_{}.dump"
    dump_list_of_pdb_ids = prj_dir + "list_of_pdb_ids.dump"
    dump_svm_profile_template = profiling_dir + "svm_profile_{}.dump"
    dump_svm_model_template = prj_dir + "models/svm_model_{}_C{}_G{}.dump"

    # paths for prediction
    prediction_svm_template = prj_dir + "predictions/svm/predictions_{}_C{}_G{}.dump"
    prediction_gor_template = prj_dir + "predictions/gor/predictions_{}.dump"
    prediction_gor_template_blind = prj_dir + "predictions/gor/predictions_blind{}.dump"
    prediction_svm_template_blind = prj_dir + "predictions/svm/predictions.dump"

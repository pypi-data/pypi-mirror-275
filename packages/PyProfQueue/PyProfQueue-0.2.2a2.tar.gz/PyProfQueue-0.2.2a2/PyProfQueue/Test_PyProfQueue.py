import PyProfQueue as ppq

ProfileScript = ppq.Script(queue_system='slurm',
                           work_script='/home/marcuskeil/Projects/RSE/Profiling/BashTests/example.sh',
                           read_queue_system='slurm',
                           profiling={
                               "linaro_forge": {
                                   'code_line': [""],
                                   'work_script': [""]
                               }
                           },
                           queue_options={
                               'workdir':
                                   '/home/marcuskeil/Projects/RSE/Package_Development/PyProfQueue/test_work/%x.%j',
                               'account': 'durham',
                               'cores': '16',
                               'nodes': '1',
                               'output': '/cosma5/data/do011/dc-keil1/TestFiles/Results/logs/%x.%j.out',
                               'partition': 'cosma',
                               'name': 'NoneToSlurm',
                               'tasks': '1',
                               'time': '03:00:00'
                           })

ppq.submit(ProfileScript,
           tmp_work_script='/home/marcuskeil/Projects/RSE/Package_Development/Test/tmp_work.sh',
           tmp_profile_script='/home/marcuskeil/Projects/RSE/Package_Development/Test/tmp_profile.sh',
           bash_options=['/cosma5/data/do011/dc-keil1/TestFiles/Codes/export_variables.source', '${WORKING_DIR}'],
           leave_scripts=True,
           test=True)

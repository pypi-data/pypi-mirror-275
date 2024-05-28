def is_elf(elf_path):
    # TODO: check file header and first bytes to determine the file type
    return True


def analyze_elf(elf_path, test_battery=None, verbosity=0):
    # re.fullmatch('a', "") is None
    if not is_elf(elf_path):
        print(f'[WARN] File "{elf_path}" is not an ELF. Skipping')
    if test_battery is None or len(test_battery) == 0:
        # By default, all tests are executed
        # test_battery = _ALL_TESTS
        pass
    if verbosity >= 1:
        print(f'[INFO] Analyzing file {elf_path}. Total number of tests: {len(test_battery)}')
    for t in test_battery:
        if verbosity >= 2:
            print(f'[INFO] Executing samples {t}')
        # Do things
        # Once it is completed
        if verbosity >= 2:
            print(f'[INFO] Test {t} completed. Result: positive. Time elapsed 0.02s')
    if verbosity >= 1:
        print(f'[INFO] File {elf_path} analyzed. Time elapsed: 20s')

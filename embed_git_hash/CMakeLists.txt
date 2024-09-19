################################################################################
#  Configure Build Info
################################################################################

execute_process(
    COMMAND git log -1 --format=%H
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    OUTPUT_VARIABLE GIT_COMMIT_HASH
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

configure_file(BuildConfig.h.in
    BuildConfig.h
    @ONLY)

configure_file(BuildConfig.json.in
    BuildConfig.json
    @ONLY)

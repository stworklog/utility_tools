# Examples of using cantools to decode can data using dbc files
# https://github.com/cantools/cantools

# Replace HEEL_SPEEDS.WHEEL with the keyword.
# You need to read the dbc to find the keyword

cat can_log.txt | python3 -m cantools plot motohawk.dbc '*WHEEL_SPEEDS.WHEEL*'

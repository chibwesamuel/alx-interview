# Star Wars API Script

This is a script that retrieves and displays the characters of a specific Star Wars movie using the Star Wars API. The script takes a Movie ID as an argument and fetches the characters associated with that movie, displaying their names line by line.

## Prerequisites

Before running the script, you need to have Node.js 10 and the `semistandard` and `request` modules installed.

### Install Node.js 10

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install `semistandard`

```bash
$ sudo npm install semistandard --global
```

### Install `request` module

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Usage

Run the script with the desired Movie ID as the first positional argument. The script will fetch and display the characters associated with the specified movie.

```bash
$ ./0-starwars_characters.js <Movie_ID>
```

Example:

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Repository Structure

The code for this project is available in the following GitHub repository:

- Repository: [alx-interview](https://github.com/chibwesamuel/alx-interview)
- Directory: 0x06-starwars_api
- File: 0-starwars_characters.js

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This script utilizes the Star Wars API to retrieve character information.
- Thanks to the developers of the Star Wars API for providing the data.

Feel free to reach out with any questions or improvements! 🚀

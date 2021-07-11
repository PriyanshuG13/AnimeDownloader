# AnimeDownloader 

                                                          ___           ___                       ___           ___     
                                                         /  /\         /__/\        ___          /__/\         /  /\    
                                                        /  /::\        \  \:\      /  /\        |  |::\       /  /:/_   
                                                       /  /:/\:\        \  \:\    /  /:/        |  |:|:\     /  /:/ /\  
                                                      /  /:/~/::\   _____\__\:\  /__/::\      __|__|:|\:\   /  /:/ /:/_ 
                                                     /__/:/ /:/\:\ /__/::::::::\ \__\/\:\__  /__/::::| \:\ /__/:/ /:/ /\
                                                     \  \:\/:/__\/ \  \:\~~\~~\/    \  \:\/\ \  \:\~~\__\/ \  \:\/:/ /:/
                                                      \  \::/       \  \:\  ~~~      \__\::/  \  \:\        \  \::/ /:/ 
                                                       \  \:\        \  \:\          /__/:/    \  \:\        \  \:\/:/  
                                                        \  \:\        \  \:\         \__\/      \  \:\        \  \::/   
                                                         \__\/         \__\/                     \__\/         \__\/    
                     _____          ___           ___           ___                         ___           ___          _____          ___           ___     
                    /  /::\        /  /\         /__/\         /__/\                       /  /\         /  /\        /  /::\        /  /\         /  /\    
                   /  /:/\:\      /  /::\       _\_ \:\        \  \:\                     /  /::\       /  /::\      /  /:/\:\      /  /:/_       /  /::\   
                  /  /:/  \:\    /  /:/\:\     /__/\ \:\        \  \:\    ___     ___    /  /:/\:\     /  /:/\:\    /  /:/  \:\    /  /:/ /\     /  /:/\:\  
                 /__/:/ \__\:|  /  /:/  \:\   _\_ \:\ \:\   _____\__\:\  /__/\   /  /\  /  /:/  \:\   /  /:/~/::\  /__/:/ \__\:|  /  /:/ /:/_   /  /:/~/:/  
                 \  \:\ /  /:/ /__/:/ \__\:\ /__/\ \:\ \:\ /__/::::::::\ \  \:\ /  /:/ /__/:/ \__\:\ /__/:/ /:/\:\ \  \:\ /  /:/ /__/:/ /:/ /\ /__/:/ /:/___
                  \  \:\  /:/  \  \:\ /  /:/ \  \:\ \:\/:/ \  \:\~~\~~\/  \  \:\  /:/  \  \:\ /  /:/ \  \:\/:/__\/  \  \:\  /:/  \  \:\/:/ /:/ \  \:\/:::::/
                   \  \:\/:/    \  \:\  /:/   \  \:\ \::/   \  \:\  ~~~    \  \:\/:/    \  \:\  /:/   \  \::/        \  \:\/:/    \  \::/ /:/   \  \::/~~~~ 
                    \  \::/      \  \:\/:/     \  \:\/:/     \  \:\         \  \::/      \  \:\/:/     \  \:\         \  \::/      \  \:\/:/     \  \:\     
                     \__\/        \  \::/       \  \::/       \  \:\         \__\/        \  \::/       \  \:\         \__\/        \  \::/       \  \:\    
                                   \__\/         \__\/         \__\/                       \__\/         \__\/                       \__\/         \__\/    
                                                     ___           ___           ___                       ___               
                                                    /  /\         /  /\         /  /\        ___          /  /\        ___   
                                                   /  /:/_       /  /:/        /  /::\      /  /\        /  /::\      /  /\  
                                                  /  /:/ /\     /  /:/        /  /:/\:\    /  /:/       /  /:/\:\    /  /:/  
                                                 /  /:/ /::\   /  /:/  ___   /  /:/~/:/   /__/::\      /  /:/~/:/   /  /:/   
                                                /__/:/ /:/\:\ /__/:/  /  /\ /__/:/ /:/___ \__\/\:\__  /__/:/ /:/   /  /::\   
                                                \  \:\/:/~/:/ \  \:\ /  /:/ \  \:\/:::::/    \  \:\/\ \  \:\/:/   /__/:/\:\  
                                                 \  \::/ /:/   \  \:\  /:/   \  \::/~~~~      \__\::/  \  \::/    \__\/  \:\ 
                                                  \__\/ /:/     \  \:\/:/     \  \:\          /__/:/    \  \:\         \  \:\
                                                    /__/:/       \  \::/       \  \:\         \__\/      \  \:\         \__\/
                                                    \__\/         \__\/         \__\/                     \__\/              


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is an Anime Downloader which also keeps track of your Anime records using json database.
Well it started as an automation for my daily use. But then I thought of making a full fleshed project for others. 

This Python Project keeps can help you maintain an Anime Database in form of **JSON**.

Basically there will be two tables in that database.
1. To keep track of your **watched/watching/wishTo** Anime List with all the essential details about the Anime.
2. To keep track of your **currently_airing/watching_live_episodes** Anime List for Download.

For Download, it Uses Torrent. So I recommend you to download a torrent client.
My preferred torrent client is **[Free Download Manager](https://www.freedownloadmanager.org)**.


### Built With

* [Python](https://getbootstrap.com)
* [JSON](https://jquery.com)


<!-- GETTING STARTED -->
## Getting Started

This is to help you get started on the on how-to set up the project for your use.

### Prerequisites

#### macOS

* python3
  ```sh
  brew install python
  python -m pip install
  python -v
  pip install pipenv
  ```

* figlet
  
  For using fonts like above in terminal.
  ```sh
  brew install figlet
  ```

* lolcat
  
  For using colorful text in terminal.
  * RubyGem
    ```sh
    ruby -v #to check if already installed
    brew install ruby # install
    ruby -v
    ```
  ```shell
  gem -v
  gem install lolcat
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/PriyanshuG13/AnimeDownloader.git
   ```
2. Install python dependencies
   ```sh
   pipenv install
   ```

<!-- USAGE EXAMPLES -->
## Usage

### For Running

```
cd ./Directory of Project
pipenv shell
python .
exit #for exiting pipenv shell
```

### Database Interactions

#### For inserting to database

* for single insert
    ```
    python Database <table_name> insert <input>
  
    #python Database downloader insert [SubsPlease],Boku No Hero Academia,N/A,(1080p),(SUB),Saturday,100
    ```
* for multiple insert
    ```
    python Database <table_name> insert multiple
  
    #python Database downloader insert multiple
    ```

#### For updating value in database

```
python Database <table_name> update <indexFrom0> <columnToUpdate> <newValue>

# Updating first row
# python Database downloader update 0 EP 8
```

#### For deleting from database

```
python Database <table_name> delete <indexfrom0>

# Deleting first row
# python Database downloader delete 0
```

#### For displaying table from database

```
python Database <table_name> show

# python Database downloader show
```

<!-- CONTRIBUTING 
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
-->

<!-- 
## License
Distributed under the MIT License. See `LICENSE` for more information.
-->


<!-- CONTACT -->
## Contact

Priyanshu Gupta - [@P_G_1_3](https://twitter.com/your_username) - priyanshu.g1312@gmail.com

Project Link: [https://github.com/PriyanshuG13/AnimeDownloader.git](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Free Download Manager](https://www.freedownloadmanager.org)
* [nyaa.iss.one](https://nyaa.iss.one)
* [Homebrew](https://brew.sh)
* [RubyGem](https://www.ruby-lang.org/en/)
* [figlet](http://www.figlet.org)
* [lolcat](https://github.com/busyloop/lolcat.git)
* [Requests](https://pypi.org/project/requests/)
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
* [pyFiglet](https://pypi.org/project/pyfiglet/)


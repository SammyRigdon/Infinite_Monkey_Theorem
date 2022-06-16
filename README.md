<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<h3 align="center">Infinite Monkey Theorem</h3>

  <p align="center">
    This project randomly generates characters in an attempt to recreate a selected document.
    <br />
    <a href="https://github.com/SammyRigdon/Infinite_Monkey_Theorem"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SammyRigdon/Infinite_Monkey_Theorem/issues">Report Bug</a>
    ·
    <a href="https://github.com/SammyRigdon/Infinite_Monkey_Theorem/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was inspired by the <a href="https://en.wikipedia.org/wiki/Infinite_monkey_theorem">The Infinite Monkey Theorem</a> and the <a href=https://libraryofbabel.info/>Library of Babel</a> project created by <a href=https://jonathanbasile.info/>Johnathan Blaise</a>. While it is not capable of replicating the full thought experiment it does allow for the use of random characters to generate any text document. This project was built entirely in Python using only the standard libraries.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.8](https://python.org/)
* [Glob](https://docs.python.org/3/library/glob.html)
* [Multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Python 3.8 or above required for use

### Installation

1. [Install Python](https://python.org)
2. Ensure Python installed correctly  by opening console and entering python. Output should be similar to below
   ```sh
   Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   ```
3. Clone the repo
   ```sh
   git clone https://github.com/SammyRigdon/Infinite_Monkey_theorem.git
   ```
4. Add any .txt documents you wish to clone to the Samples Directory

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the script using the following command
   ```sh
   python [path_to_script]/main.py
   ```
Follow the prompts then allow the system to work. There are two modes currently: character mode and word mode.

In character mode the monkeys will be given a specific character to search for. They will generate a random character until they get one that matches. This is the fastest method and can generate documnets in a few minutes. Word mode has each monkey attempting to generate specific words. This process is much more random, where as each process in character mode has a 1 in 121 chance of happening, the chances of just a three character word being successfully generated in 1 in 1.95 million **THIS IS VERY INTESE ON YOUR CPU AND WILL TAKE A LONG TIME**

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] True Infinite Monkey Theorem
- [ ] Random Order Character Generation
- [ ] Random Order Word Generation

See the [open issues](https://github.com/SammyRigdon/Infinite_Monkey_theorem/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Sammy Rigdon - sammyrigdon496@gmail.com

Project Link: [https://github.com/SammyRigdon/Infinite_Monkey_Theorem](https://github.com/SammyRigdon/Infinite_Monkey_Theorem)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Below are resources and people who helped me on this project. I used while working on this project. Thank you to all the individuals who helped my along the way.
* [README Template by othneildrew](https://github.com/othneildrew) 
* [r/LearnPython](https://www.reddit.com/r/learnpython/)
* [Pyhton Documentation](https://www.python.org/doc/)
* [Larry Payne](https://www.linkedin.com/in/larry-payne-069557108/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SammyRigdon/Infinite_Monkey_Theorem.svg?style=for-the-badge
[contributors-url]: https://github.com/SammyRigdon/Infinite_Monkey_Theorem/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SammyRigdon/Infinite_Monkey_Theorem.svg?style=for-the-badge
[forks-url]: https://github.com/SammyRigdon/Infinite_Monkey_Theorem/network/members
[stars-shield]: https://img.shields.io/github/stars/SammyRigdon/Infinite_Monkey_Theorem.svg?style=for-the-badge
[stars-url]: https://github.com/SammyRigdon/Infinite_Monkey_Theorem/stargazers
[issues-shield]: https://img.shields.io/github/issues/SammyRigdon/Infinite_Monkey_Theorem.svg?style=for-the-badge
[issues-url]: https://github.com/SammyRigdon/Infinite_Monkey_Theorem/issues
[license-shield]: https://img.shields.io/github/license/SammyRigdon/Infinite_Monkey_Theorem.svg?style=for-the-badge
[license-url]: https://github.com/SammyRigdon/Infinite_Monkey_Theorem/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sammy-rigdon-82089a208
[product-screenshot]: images/screenshot.png

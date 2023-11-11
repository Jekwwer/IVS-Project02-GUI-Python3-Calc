<h1 align="center">🌊 WaterLift Calculator</h1>
<p align="center">
    <img src="https://i.ibb.co/sH7mC4S/waterlift-calculator-logo.png" alt="waterlift_calculator_logo" border="0">
</p>

_WaterLift Calculator_ is a calculator application that provides basic mathematical operations designed for comfortable home counting.

This application was developed as the second project for the _"Practical Aspects of Software Design"_ school subject by the team _"Blue Hair is the Way"_.

## 💻 Supported platforms

The application works properly on **Ubuntu 20.04 64-bit** or newer.

## 🔗 Dependencies

-   `python3.8`: The core programming language used by WaterLift Calculator.
-   `python-tk`: A graphical user interface (GUI) library for Python-based applications.
-   `python3-pip`: The package installer for Python, allowing you to install other necessary packages.
-   `tkDocViewer`: A Tkinter-based widget to display text documents in various formats.

## 📥 Installation

[Download the latest version of the application installer here.](https://github.com/Jekwwer/IVS-Project02-WaterLift-Calc/releases)

-   Open the installer and click the **Install** button.
<p align="center">
    <img src="https://i.ibb.co/crXMWL8/installation.png" alt="installation" border="0">
</p>

-   Or use the CLI command:

```bash
sudo dpkg -i waterlift_calc-1.0-ubuntu20.04-x64.deb
```

## ▶️ Run WaterLift Calculator

-   Go to 'Show Applications' and click on _WaterLift Calculator_.
<p align="center">
    <img src="https://i.ibb.co/DLtywF2/run-from-the-show-application.png" alt="run_from_the_show_application" border="0">
</p>

-   Or use the CLI command:

```bash
waterlift-calc
```

## ✨ Features

#### "No zero part"

No need to write a zero in decimal numbers; the calculator adds it by itself.

<p align="center">
    <img src="https://i.ibb.co/PMgxJTM/no-zero-part.gif" alt="no_zero_part" border="0">
</p>

#### "Continue the calculating"

After the evaluation of the last expression,

-   Press `=` to put the result into the input field
<p align="center">
    <img src="https://i.ibb.co/pxMPvSr/continue-the-calculating01.gif" alt="continue_the_calculating01" border="0">
</p>

-   Or press the operation sign (except `√`,`㏒`, `㏑`) to put the result into the input field with it
<p align="center">
    <img src="https://i.ibb.co/7RFC5tg/continue-the-calculating02.gif" alt="continue_the_calculating02" border="0">
</p>

#### "Change the operation sign"

When you put an operation sign into the input field, you can change it by pressing another.

<p align="center">
    <img src="https://i.ibb.co/Wx9BDKy/change-the-operation-sign.gif" alt="change_the_operation_sign" border="0">
</p>

#### Window size control

You can change the window size by clicking the `left mouse button` on the sizegrip and moving the mouse.

<p align="center">
    <img src="https://i.ibb.co/RTt5NyP/window-size-control.gif" alt="window_size_control" border="0">
</p>

#### Inactive buttons

The buttons become inactive if their using is impossible in the current expression.

#### Keyboard input support

We provide keyboard support for all input buttons. You can find _Keyboard bindings table_ in the [user manual](./documentation.pdf).

#### In-build user manual

You can always open a short version of the user manual by clicking `Help` or pressing the `H` keyboard button.

<p align="center">
    <img src="https://i.ibb.co/sqyp9B6/help-window.gif" alt="help_window" border="0">
</p>

## 🎨 Appearance

<p align="center">
    <img src="https://i.ibb.co/YXdmGvM/user-interface01.png" alt="user_interface01" border="0">
</p>

We also provide some color themes for your better calculating experience.

<p align="center">
    <img src="https://i.ibb.co/bHP3CQP/ui-color-themes.gif" alt="ui_color_themes" border="0">
</p>

## 📅 Plans

In the future, we are planning to add:

-   Scientific mode
-   Graph plotting
-   Memory keys support

<p align="center">
    <img src="https://i.ibb.co/M686gwb/mockup.png" alt="mockup" border="0">
</p>

## 🔑 License

[GNU GPLv3 ](LICENSE)

## 👤 Authors - Blue Hair is the Way

| Member            | Project Parts                                               |
| :---------------- | :---------------------------------------------------------- |
| Evgenii Shiliaev  | GUI logic, mathematical library, user documentation, mockup |
| Pavel Beneš       | tests, program documentation, keyboard input                |
| Šimon Brázda      | profiling, installer                                        |
| Marko Kubrachenko | GUI appearance, mathematical library, Makefile              |

---

<h1 align="center">🌊 Happy calculating!</h1>

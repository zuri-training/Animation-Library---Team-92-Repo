Moov
Introduction
Moov is an open source library that allows beginners perform basic web animation using normal language,the Moov library allows users add animations to the websites.

Usage
Download the zip folder:

CSS FILE:

<link rel="stylesheet" href="path/moov-animate.min.css">

HTML STRUCTURE:

    <div class="moov-moveUp">
        <div>Section 1</div>
        <div>Section 2</div>
        <div>Section 3</div>
    </div>

</div>

## Example

This basic code is to apply a bouceIn animation:
Example
This basic code is to appply a bouceIn animation:

<div class="moov-bounceIn"></div>
To add a glow animation;

<div class="moov-glow"></div>
you can check for more usage examples on the website. - [ ]uncompleted

Contribution
If you want to contribute to this project,a pull request is the way to go and make sure to use standalized class-names.

You can view more about the Moov documentation on the website

#How to work with repo locally:
1) clone the repository
2) cd to moov_website


Download from here

Import it into your file:

import ‘moov.css';

If you are using an HTML structure you can also add to As

Or add it directly to your webpage using a CDN:

Basic usage After adding or embedding the moov.css library to your code, Always ensure before calling your animation name you include “moov_animated” then the animation name.


# Best Practices

Animation has a great way of calling users' attention to view your website more but it is super important you use animations in places where they are needed. There are some basic rules to follow so you stay on track while using any animation library.

Good usage of animations A component shouldn't be animated merely in order to create animation. Take into consideration that movements ought to be explicit in their intentions. Instead of just adding "flashiness" to your interface, movements including exhibitionists (bounce, blink, etc.) should be utilized to draw the attention of the user to anything exceptional in it.

Use exit and entry movements to point out exactly what is occurring in the interaction and make it evident when it is changing states.



The CSS property animation-fill-mode, which regulates an element's states before and after animation, is a component of every Moov.css animation. Learn more about it by visiting this page. The animation-fill-mode setting in Moov.css is both by default, but you can modify it to meet your specific requirements.

# Some usage that can’t be avoided

Despite the fact that some browsers support inline animation, doing so violates the CSS animation specifications and will eventually malfunction or stop working on some browsers. Always animate items at the block or inline-block level (grid and flex containers and children are block-level elements too). When animating an inline-level element, you can set the element to display: inline-block.




  #   Utility Classes

A few utility classes are included with Moov.css to make use of it easier.

Delayed classes Delays can be added straight to the element's class attribute as shown here:

Try this
Moov.css provides different types of delay animations from 1s to 2s etc.
The delays offer ranges from 1s to 2s. You can alter them by adjusting the moov_delay property’s duration to a longer or shorter time frame.

/_ All delay classes will take 2x longer to start _/ :root { --moov-delay: 1s; }

/_ All delay classes will take half the time to start _/ :root { --moov-delay: 2s; }

lessons in slow, slower, fast, and faster

By including these classes, as shown below, you can modify the animation's speed:

Try this
Moov.css provides different types of fast ,faster,slow,slower animations from 1s to 2s etc.

The default speed for the moov_animated class is1s to 2s. Additionally, you can locally or globally alter the animations' duration with the - -moov-duration parameter. Both the utility classes and the animation classes will be impacted by this.

Example:

/_ All animations will take twice as long to finish _/ :root { --moov-duration: 1.2s; }

/_ Only this element will take half the time to finish _/ .my-element { --moov-duration: 800ms; }

Take note that certain animations only last a fraction of a second,using the - -moov-duration property to determine the duration will take these into account. Therefore, all animations will adjust to changes in the global duration.

Repeating Classes By including these classes, as shown below, you can manage how many times the animation is iterated: We have different repeat properties ranging from moov_repeat-1

moov_repeat-2

moov_repeat-3

moov_infinite

The animation will be repeated twice by the element. In order to avoid a complicated situation, it is best to specify this value locally rather than globally. \*/ -- repeat-repeat: 2;

TEAM MEMBERS :

Adesewa Adeboye - Product Design
Charles - Product Design
Prosper - Product Design
Hillz - Product Design
Jomex - Product Design
Kolavic - Product Design
Oluwatosin - Product Design
Peace - Product Design
Snazzyvee - Product Design
Tai_Cee - Product Design
Taofiqah - Product Design
Tessie - Product Design
Adetayo - Fullstack
Blessing Garba - Fullstack
Darhniel - Fullstack
Kenechukwu - Fullstack
Okechukwu - Fullstack
Oluwatoyin - Fullstack
Tallmantek (David)- Fullstack
Tams - Fullstack
Patrick – Frontend

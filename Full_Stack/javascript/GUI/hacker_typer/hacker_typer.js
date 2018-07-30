let dummyText = "" +
    "<!DOCTYPE html>\n" +
    "<html lang=\"en\">\n" +
    "\n" +
    "<head>\n" +
    "    <meta charset=\"utf-8\">\n" +
    "    <title>CSS Zen Garden: The Beauty of CSS Design</title>\n" +
    "\n" +
    "    <!-- <link rel=\"stylesheet\" media=\"screen\" href=\"beginner_style.css\"> -->\n" +
    "    <!-- <link rel=\"stylesheet\" media=\"screen\" href=\"advanced_style.css\"> -->\n" +
    "    <link rel=\"stylesheet\" media=\"screen\" href=\"xtra_advanced_style.css\">\n" +
    "    <!--<link rel=\"stylesheet\" media=\"screen\" href=\"xxtra_advanced_style.css\">-->\n" +
    "    <!-- <link rel=\"stylesheet\" media=\"screen\" href=\"xxxtra_advanced_style.css\"> -->\n" +
    "\n" +
    "    <link rel=\"alternate\" type=\"application/rss+xml\" title=\"RSS\" href=\"http://www.csszengarden.com/zengarden.xml\">\n" +
    "\n" +
    "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" +
    "    <meta name=\"author\" content=\"Dave Shea\">\n" +
    "    <meta name=\"description\" content=\"A demonstration of what can be accomplished visually through CSS-based design.\">\n" +
    "    <meta name=\"robots\" content=\"all\">\n" +
    "\n" +
    "    <!--[if lt IE 9]>\n" +
    "\t<script src=\"script/html5shiv.js\"></script>\n" +
    "\t<![endif]-->\n" +
    "    <style>\n" +
    "    @import url('https://fonts.googleapis.com/css?family=Muli');\n" +
    "        \n" +
    "        * {\n" +
    "            box-sizing: border-box;\n" +
    "        }\n" +
    "        \n" +
    "        html, body {\n" +
    "            height: 100%;\n" +
    "            margin: 0;\n" +
    "            font-family: 'Muli', sans-serif;\n" +
    "            color: white;\n" +
    "        }\n" +
    "        \n" +
    "        h1, h2 {\n" +
    "            font-size: 50px;\n" +
    "        }\n" +
    "        \n" +
    "        header {\n" +
    "            background-color: #fc783e;\n" +
    "            padding: 20px 100px 1px;\n" +
    "            margin-right: 3px;\n" +
    "        }\n" +
    "        \n" +
    "        .summary {\n" +
    "            background-color: #fc783e;\n" +
    "            font-size: 15px;\n" +
    "            padding: 1px 100px 20px;\n" +
    "            margin-bottom: 3px;\n" +
    "            margin-right: 3px;\n" +
    "        }\n" +
    "        \n" +
    "        .summary a {\n" +
    "            color: #fbca03;\n" +
    "        }\n" +
    "        \n" +
    "        .preamble {\n" +
    "            background: linear-gradient(\n" +
    "                    rgba(121, 85, 72, 0.45),\n" +
    "                    rgba(121, 85, 72, 0.45)\n" +
    "            ), url(https://upload.wikimedia.org/wikipedia/commons/9/9d/CSIRO_ScienceImage_3176_Arabidopsis_in_growth_cabinet_at_the_CSIRO_Discovery_Centre_labs_Black_Mountain_ACT.jpg);\n" +
    "        }\n" +
    "        \n" +
    "        .explanation {\n" +
    "            background-image: url(https://static.pexels.com/photos/4700/nature-forest-moss-leaves.jpg);\n" +
    "        }\n" +
    "        \n" +
    "        .participation {\n" +
    "            background: linear-gradient(\n" +
    "                    rgba(121, 85, 72, 0.45),\n" +
    "                    rgba(121, 85, 72, 0.45)\n" +
    "            ), url(http://www.lovethispic.com/uploaded_images/223291-Nature.jpg);\n" +
    "        }\n" +
    "        \n" +
    "        .participation a {\n" +
    "            color: #fbca03;\n" +
    "        }\n" +
    "        \n" +
    "        .benefits {\n" +
    "            background-image: url(https://visualhunt.com/photos/1/close-up-of-sunflower.jpg?s=xl);\n" +
    "            margin-bottom: 3px;\n" +
    "        }\n" +
    "        \n" +
    "        .preamble, .explanation, .participation, .benefits {\n" +
    "            background-position: center;\n" +
    "            background-attachment: fixed;\n" +
    "            background-size: cover;\n" +
    "            font-size: 30px;\n" +
    "            padding: 75px;\n" +
    "        }\n" +
    "        \n" +
    "        .requirements, footer {\n" +
    "            display: none;\n" +
    "        }\n" +
    "        \n" +
    "        .sidebar a {\n" +
    "            text-decoration: none;\n" +
    "        }\n" +
    "        \n" +
    "        .wrapper {\n" +
    "            display: flex;\n" +
    "            flex-wrap: wrap;\n" +
    "        }\n" +
    "        \n" +
    "        .wrapper ul {\n" +
    "            list-style: none;\n" +
    "        }\n" +
    "        \n" +
    "        .wrapper h3, .design-selection li :first-child {\n" +
    "            font-size: 35px;\n" +
    "        }\n" +
    "        \n" +
    "        .wrapper li :not(:first-child) {\n" +
    "            font-size: 20px;\n" +
    "        }\n" +
    "        \n" +
    "        .design-selection {\n" +
    "            background-color: #fc783e;\n" +
    "            color: rgba(88, 60, 50, 0.58);\n" +
    "            width: 100vw;\n" +
    "            height: 80vh;\n" +
    "            display: flex;\n" +
    "            flex-direction: column;\n" +
    "            justify-content: center;\n" +
    "            align-items: center;\n" +
    "        }\n" +
    "        \n" +
    "        .design-selection h3 {\n" +
    "            color: white;\n" +
    "        }\n" +
    "        \n" +
    "        .design-selection li a:first-of-type {\n" +
    "            color: #333;\n" +
    "        }\n" +
    "        \n" +
    "        .design-selection li a:last-of-type {\n" +
    "            color: white;\n" +
    "        }\n" +
    "        \n" +
    "        .design-selection ul {\n" +
    "            display: flex;\n" +
    "            flex-wrap: wrap;\n" +
    "        }\n" +
    "        \n" +
    "        .design-selection li {\n" +
    "            display: flex;\n" +
    "            flex-direction: column;\n" +
    "            text-align: center;\n" +
    "            padding-top: 20px;\n" +
    "            width: 25%;\n" +
    "        }\n" +
    "        \n" +
    "        .design-archives, .zen-resources {\n" +
    "            display: flex;\n" +
    "            flex-direction: column;\n" +
    "            justify-content: center;\n" +
    "            align-items: center;\n" +
    "        }\n" +
    "        \n" +
    "        .design-archives ul, .zen-resources ul {\n" +
    "            display: flex;\n" +
    "            padding: 0px;\n" +
    "        }\n" +
    "        \n" +
    "        .design-archives a, .zen-resources a {\n" +
    "            font-size: 20px;\n" +
    "            padding-right: 10px;\n" +
    "        }\n" +
    "        \n" +
    "        .design-archives {\n" +
    "            width: 50vw;\n" +
    "            height: 50vh;\n" +
    "            background-color: #333;\n" +
    "        }\n" +
    "        \n" +
    "        .design-archives a {\n" +
    "            color: #fc783e;\n" +
    "        }\n" +
    "        \n" +
    "        .zen-resources {\n" +
    "            width: 50vw;\n" +
    "            height: 50vh;\n" +
    "            background-color: #2196f3;\n" +
    "        }\n" +
    "        \n" +
    "        .zen-resources a {\n" +
    "            color: #333;\n" +
    "        }\n" +
    "\n" +
    "    </style>\n" +
    "</head>\n" +
    "\n" +
    "<!--\n" +
    "\tView source is a feature, not a bug. Thanks for your curiosity and\n" +
    "\tinterest in participating!\n" +
    "\tHere are the submission guidelines for the new and improved csszengarden.com:\n" +
    "\t- CSS3? Of course! Prefix for ALL browsers where necessary.\n" +
    "\t- go responsive; test your layout at multiple screen sizes.\n" +
    "\t- your browser testing baseline: IE9+, recent Chrome/Firefox/Safari, and iOS/Android\n" +
    "\t- Graceful degradation is acceptable, and in fact highly encouraged.\n" +
    "\t- use classes for styling. Don't use ids.\n" +
    "\t- web fonts are cool, just make sure you have a license to share the files. Hosted\n" +
    "\t  services that are applied via the CSS file (ie. Google Fonts) will work fine, but\n" +
    "\t  most that require custom HTML won't. TypeKit is supported, see the readme on this\n" +
    "\t  page for usage instructions: https://github.com/mezzoblue/csszengarden.com/\n" +
    "\tAnd a few tips on building your CSS file:\n" +
    "\t- use :first-child, :last-child and :nth-child to get at non-classed elements\n" +
    "\t- use ::before and ::after to create pseudo-elements for extra styling\n" +
    "\t- use multiple background images to apply as many as you need to any element\n" +
    "\t- use the Kellum Method for image replacement, if still needed. http://goo.gl/GXxdI\n" +
    "\t- don't rely on the extra divs at the bottom. Use ::before and ::after instead.\n" +
    "\n" +
    "-->\n" +
    "\n" +
    "<body id=\"css-zen-garden\">\n" +
    "    <div class=\"page-wrapper\">\n" +
    "\n" +
    "        <section class=\"intro\" id=\"zen-intro\">\n" +
    "            <header role=\"banner\">\n" +
    "                <h1>CSS Zen Garden</h1>\n" +
    "                <h2>The Beauty of CSS Design</h2>\n" +
    "            </header>\n" +
    "\n" +
    "            <div class=\"summary\" id=\"zen-summary\">\n" +
    "                <p>A demonstration of what can be accomplished through CSS-based design. Select any style sheet from the list to load it into this page.</p>\n" +
    "                <p>Download the example\n" +
    "                    <a href=\"/examples/index\" title=\"This page's source HTML code, not to be modified.\">\n" +
    "                        html file\n" +
    "                    </a>\n" +
    "                    and\n" +
    "                    <a href=\"/examples/style.css\" title=\"This page's sample CSS, the file you may modify.\"\n" +
    "                       >css file\n" +
    "                    </a>\n" +
    "                </p>\n" +
    "            </div>\n" +
    "\n" +
    "            <div class=\"preamble\" id=\"zen-preamble\">\n" +
    "                <h3>The Road to Enlightenment</h3>\n" +
    "                <p>Littering a dark and dreary road lay the past relics of browser-specific tags, incompatible DOMs, broken CSS support, and abandoned browsers.</p>\n" +
    "                <p>We must clear the mind of the past. Web enlightenment has been achieved thanks to the tireless efforts of folk like the W3C, WaSP, and the major browser creators.</p>\n" +
    "                <p>The CSS Zen Garden invites you to relax and meditate on the important lessons of the masters. Begin to see with clarity. Learn to use the time-honored techniques in new and invigorating fashion. Become one with the web.</p>\n" +
    "            </div>\n" +
    "        </section>\n" +
    "\n" +
    "        <div class=\"main supporting\" id=\"zen-supporting\">\n" +
    "            <div class=\"explanation\" id=\"zen-explanation\">\n" +
    "                <h3>So What is This About?</h3>\n" +
    "                <p>There is a continuing need to show the power of CSS. The Zen Garden aims to excite, inspire, and encourage participation. To begin, view some of the existing designs in the list. Clicking on any one will load the style sheet into this very page. The HTML remains the same, the only thing that has changed is the external CSS file. Yes, really.</p>\n" +
    "                <p>CSS allows complete and total control over the style of a hypertext document. The only way this can be illustrated in a way that gets people excited is by demonstrating what it can truly be, once the reins are placed in the hands of those able to create beauty from structure. Designers and coders alike have contributed to the beauty of the web; we can always push it further.</p>\n" +
    "            </div>\n" +
    "\n" +
    "            <div class=\"participation\" id=\"zen-participation\">\n" +
    "                <h3>Participation</h3>\n" +
    "                <p>Strong visual design has always been our focus. You are modifying this page, so strong CSS skills are necessary too, but the example files are commented well enough that even CSS novices can use them as starting points. Please see the <a href=\"http://www.mezzoblue.com/zengarden/resources/\">CSS Resource Guide</a> for advanced tutorials and tips on working with CSS.</p>\n" +
    "                <p>You may modify the style sheet in any way you wish, but not the HTML. This may seem daunting at first if you've never worked this way before, but follow the listed links to learn more, and use the sample files as a guide.</p>\n" +
    "                <p>Download the sample <a href=\"/examples/index\">HTML</a> and <a href=\"/examples/style.css\">CSS</a> to work on a copy locally. Once you have completed your masterpiece (and please, don't submit half-finished work) upload your CSS file to a web server under your control. <a href=\"http://www.mezzoblue.com/zengarden/submit/\" >Send us a link</a> to an archive of that file and all associated assets, and if we choose to use it we will download it and place it on our server.</p>\n" +
    "            </div>\n" +
    "\n" +
    "            <div class=\"benefits\" id=\"zen-benefits\">\n" +
    "                <h3>Benefits</h3>\n" +
    "                <p>Why participate? For recognition, inspiration, and a resource we can all refer to showing people how amazing CSS really can be. This site serves as equal parts inspiration for those working on the web today, learning tool for those who will be tomorrow, and gallery of future techniques we can all look forward to.</p>\n" +
    "            </div>\n" +
    "\n" +
    "            <div class=\"requirements\" id=\"zen-requirements\">\n" +
    "                <h3>Requirements</h3>\n" +
    "                <p>Where possible, we would like to see mostly CSS 1 & 2 usage. CSS 3 & 4 should be limited to widely-supported elements only, or strong fallbacks should be provided. The CSS Zen Garden is about functional, practical CSS and not the latest bleeding-edge tricks viewable by 2% of the browsing public. The only real requirement we have is that your CSS validates.</p>\n" +
    "                <p>Luckily, designing this way shows how well various browsers have implemented CSS by now. When sticking to the guidelines you should see fairly consistent results across most modern browsers. Due to the sheer number of user agents on the web these days - especially when you factor in mobile - pixel-perfect layouts may not be possible across every platform. That's okay, but do test in as many as you can. Your design should work in at least IE9+ and the latest Chrome, Firefox, iOS and Android browsers (run by over 90% of the population).</p>\n" +
    "                <p>We ask that you submit original artwork. Please respect copyright laws. Please keep objectionable material to a minimum, and try to incorporate unique and interesting visual themes to your work. We're well past the point of needing another garden-related design.</p>\n" +
    "                <p>This is a learning exercise as well as a demonstration. You retain full copyright on your graphics (with limited exceptions, see <a href=\"http://www.mezzoblue.com/zengarden/submit/guidelines/\">submission guidelines</a>), but we ask you release your CSS under a Creative Commons license identical to the <a href=\"http://creativecommons.org/licenses/by-nc-sa/3.0/\">one on this site</a> so that others may learn from your work.</p>\n" +
    "                <p>By <a href=\"http://www.mezzoblue.com/\">Dave Shea</a>. Bandwidth graciously donated by <a href=\"http://www.mediatemple.net/\">mediatemple</a>. Now available: <a href=\"http://www.amazon.com/exec/obidos/ASIN/0321303474/mezzoblue-20/\">Zen Garden, the book</a>.</p>\n" +
    "            </div>\n" +
    "\n" +
    "            <footer>\n" +
    "                <a href=\"http://validator.w3.org/check/referer\" title=\"Check the validity of this site&#8217;s HTML\" class=\"zen-validate-html\">HTML</a>\n" +
    "                <a href=\"http://jigsaw.w3.org/css-validator/check/referer\" title=\"Check the validity of this site&#8217;s CSS\" class=\"zen-validate-css\">CSS</a>\n" +
    "                <a href=\"http://creativecommons.org/licenses/by-nc-sa/3.0/\" title=\"View the Creative Commons license of this site: Attribution-NonCommercial-ShareAlike.\" class=\"zen-license\">CC</a>\n" +
    "                <a href=\"http://mezzoblue.com/zengarden/faq/#aaa\" title=\"Read about the accessibility of this site\" class=\"zen-accessibility\">A11y</a>\n" +
    "                <a href=\"https://github.com/mezzoblue/csszengarden.com\" title=\"Fork this site on Github\" class=\"zen-github\">GH</a>\n" +
    "            </footer>\n" +
    "\n" +
    "        </div>\n" +
    "\n" +
    "\n" +
    "        <aside class=\"sidebar\" role=\"complementary\">\n" +
    "            <div class=\"wrapper\">\n" +
    "\n" +
    "                <div class=\"design-selection\" id=\"design-selection\">\n" +
    "                    <h3 class=\"select\">Select a Design:</h3>\n" +
    "                    <nav role=\"navigation\">\n" +
    "                        <ul>\n" +
    "                            <li>\n" +
    "                                <a href=\"/221/\" class=\"design-name\">Mid Century Modern</a> by <a href=\"http://andrewlohman.com/\" class=\"designer-name\">Andrew Lohman</a>\n" +
    "                            </li>\n" +
    "                            <li>\n" +
    "                                <a href=\"/220/\" class=\"design-name\">Garments</a> by <a href=\"http://danielmall.com/\" class=\"designer-name\">Dan Mall</a>\n" +
    "                            </li>\n" +
    "                            <li>\n" +
    "                                <a href=\"/219/\" class=\"design-name\">Steel</a> by <a href=\"http://steffen-knoeller.de\" class=\"designer-name\">Steffen Knoeller</a>\n" +
    "                            </li>\n" +
    "                            <li>\n" +
    "                                <a href=\"/218/\" class=\"design-name\">Apothecary</a> by <a href=\"http://trentwalton.com\" class=\"designer-name\">Trent Walton</a>\n" +
    "                            </li>\n" +
    "                            <li>\n" +
    "                                <a href=\"/217/\" class=\"design-name\">Screen Filler</a> by <a href=\"http://elliotjaystocks.com/\" class=\"designer-name\">Elliot Jay Stocks</a>\n" +
    "                            </li>\n" +
    "                            <li>\n" +
    "                                <a href=\"/216/\" class=\"design-name\">Fountain Kiss</a> by <a href=\"http://jeremycarlson.com\" class=\"designer-name\">Jeremy Carlson</a>\n" +
    "                            </li>\n" +
    "                            <li>\n" +
    "                                <a href=\"/215/\" class=\"design-name\">A Robot Named Jimmy</a> by <a href=\"http://meltmedia.com/\" class=\"designer-name\">meltmedia</a>\n" +
    "                            </li>\n" +
    "                            <li>\n" +
    "                                <a href=\"/214/\" class=\"design-name\">Verde Moderna</a> by <a href=\"http://www.mezzoblue.com/\" class=\"designer-name\">Dave Shea</a>\n" +
    "                            </li>\n" +
    "                        </ul>\n" +
    "                    </nav>\n" +
    "                </div>\n" +
    "\n" +
    "                <div class=\"design-archives\" id=\"design-archives\">\n" +
    "                    <h3 class=\"archives\">Archives:</h3>\n" +
    "                    <nav>\n" +
    "                        <ul>\n" +
    "                            <li class=\"next\">\n" +
    "                                <a href=\"/214/page1\">\n" +
    "\t\t\t\t\t\t\t\tNext Designs <span class=\"indicator\">&rsaquo;</span>\n" +
    "\t\t\t\t\t\t\t</a>\n" +
    "                            </li>\n" +
    "                            <li class=\"viewall\">\n" +
    "                                <a href=\"http://www.mezzoblue.com/zengarden/alldesigns/\">\n" +
    "\t\t\t\t\t\t\t\tView All Designs\t\t\t\t\t\t\t</a>\n" +
    "                            </li>\n" +
    "                        </ul>\n" +
    "                    </nav>\n" +
    "                </div>\n" +
    "\n" +
    "                <div class=\"zen-resources\" id=\"zen-resources\">\n" +
    "                    <h3 class=\"resources\">Resources:</h3>\n" +
    "                    <ul>\n" +
    "                        <li class=\"view-css\">\n" +
    "                            <a href=\"style.css\">\n" +
    "\t\t\t\t\t\t\tView This Design's CSS</a>\n" +
    "                        </li>\n" +
    "                        <li class=\"css-resources\">\n" +
    "                            <a href=\"http://www.mezzoblue.com/zengarden/resources/\" title=\"Links to great sites with information on using CSS.\">\n" +
    "\t\t\t\t\t\t\tCSS Resources\t</a>\n" +
    "                        </li>\n" +
    "                        <li class=\"zen-faq\">\n" +
    "                            <a href=\"http://www.mezzoblue.com/zengarden/faq/\">\n" +
    "                                <abbr title=\"Frequently Asked Questions\">FAQ</abbr> </a>\n" +
    "                        </li>\n" +
    "                        <li class=\"zen-submit\">\n" +
    "                            <a href=\"http://www.mezzoblue.com/zengarden/submit/\">\n" +
    "\t\t\t\t\t\t\tSubmit a Design\t\t\t\t\t\t</a>\n" +
    "                        </li>\n" +
    "                        <li class=\"zen-translations\">\n" +
    "                            <a href=\"http://www.mezzoblue.com/zengarden/translations/\">\n" +
    "\t\t\t\t\t\t\tTranslations\t\t\t\t\t\t</a>\n" +
    "                        </li>\n" +
    "                    </ul>\n" +
    "                </div>\n" +
    "            </div>\n" +
    "        </aside>\n" +
    "\n" +
    "\n" +
    "    </div>\n" +
    "\n" +
    "</body>\n" +
    "\n" +
    "</html>\n";

let screen = document.getElementById('myTextArea');
startIn = 0;
endIn = 10;
numPresses = 0;

// print 10 characters of text to the screen when any key is pressed
$(document).keypress(function(e) {
    e.preventDefault();
    screen.value += dummyText.slice(startIn, endIn);
    startIn = endIn;
    endIn += 10;
    screen.scrollTop = screen.scrollHeight;  // autoscroll to bottom of textarea
});
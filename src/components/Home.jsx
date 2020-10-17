import React from "react";
import { Link } from "react-router-dom";
//import about1 from "./img/about/about-1.jpg";
//import hero1 from './img/hero/hero-1.jpg';
function Home(){
        return (
            <>
                {/* Hero Section Begin */}
                <section className="hero">
                    <div className="hero__slider owl-carousel">
                        <div className="hero__item set-bg" data-setbg={require("./img/hero/hero-1.jpg")}>
                            <div className="container">
                                <div className="row">
                                    <div className="col-lg-6">
                                        <div className="hero__text">
                                            <span>building bridges for underground creators, <br /> breaking walls set by huge artists</span>
                                            <h2>Spotlight</h2>
                                            <a href="/about" className="primary-btn">See more about us</a>

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="hero__item set-bg" data-setbg={require("./img/hero/hero-1.jpg")}>
                            <div className="container">
                                <div className="row">
                                    <div className="col-lg-6">
                                        <div className="hero__text">
                                            <span>Community Driven!</span>
                                            <h2>Submit an artist now!</h2>
                                            <a href="/suggest" className="primary-btn">Submit a form!</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="hero__item set-bg" data-setbg={require("./img/hero/hero-1.jpg")}>
                            <div className="container">
                                <div className="row">
                                    <div className="col-lg-6">
                                        <div className="hero__text">
                                            <span>Want a song with a specific genre? </span>
                                            <h2>Sort by Genre</h2>
                                            <a href="/discovery" className="primary-btn">Check out our discovery page!</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <h1> hello </h1>
                {/*/!* Hero Section End *!/*/}
             {/*   /!* Services Section Begin *!/*/}
             {/*   <section className="services spad">*/}
             {/*       <div className="container">*/}
             {/*           <div className="row">*/}
             {/*               <div className="col-lg-4">*/}
             {/*                   <div className="services__title">*/}
             {/*                       <div className="section-title">*/}
             {/*                           <span>Our website</span>*/}
             {/*                           <h2>What do We do?</h2>*/}
             {/*                       </div>*/}
             {/*                       <p>Our website recommends you music based on your selected genre. To set ourselves apart form the rest of the competition, we explicitly only allow smaller creators, to allow them to gain traction easier. Millions of artists go unnoticed, because there isn't an easy way to find them. This all changes with our website.</p>*/}
             {/*                       <a href="#" className="primary-btn">Check out now!</a>*/}
             {/*                   </div>*/}
             {/*               </div>*/}
             {/*               <div className="col-lg-8">*/}
             {/*                   <div className="row">*/}
             {/*                       <div className="col-lg-6 col-md-6 col-sm-6">*/}
             {/*                           <div className="services__item">*/}
             {/*                               <div className="services__item__icon">*/}
             {/*                                   <img src="img/icons/si-1.png" alt="" />*/}
             {/*                               </div>*/}
             {/*                               <h4>Relevancy</h4>*/}
             {/*                               <p>We make sure to recommend you music that you might actually enjoy, whilst supporting smaller creators. This is very important to our website, because we make sure that we are benefiting the creator, aswell as the user of our app.</p>*/}
             {/*                           </div>*/}
             {/*                       </div>*/}
             {/*                       <div className="col-lg-6 col-md-6 col-sm-6">*/}
             {/*                           <div className="services__item">*/}
             {/*                               <div className="services__item__icon">*/}
             {/*                                   <img src="img/icons/si-2.png" alt="" />*/}
             {/*                               </div>*/}
             {/*                               <h4>Community Driven!</h4>*/}
             {/*                               <p>Our entire website is completely driven by our community, and their submissions. We do however make sure that all submissions are moderated, to ensure quality of life.</p>*/}
             {/*                           </div>*/}
             {/*                       </div>*/}
             {/*                       <div className="col-lg-6 col-md-6 col-sm-6">*/}
             {/*                           <div className="services__item">*/}
             {/*                               <div className="services__item__icon">*/}
             {/*                                   <img src="img/icons/si-3.png" alt="" />*/}
             {/*                               </div>*/}
             {/*                               <h4>spotify API</h4>*/}
             {/*                               <p>We directly connect to the spotify api to integrate directly to your spotify account, making the entire process as simple as possible.</p>*/}
             {/*                           </div>*/}
             {/*                       </div>*/}
             {/*                       <div className="col-lg-6 col-md-6 col-sm-6">*/}
             {/*                           <div className="services__item">*/}
             {/*                               <div className="services__item__icon">*/}
             {/*                                   <img src="img/icons/si-4.png" alt="" />*/}
             {/*                               </div>*/}
             {/*                               <h4>Open Source</h4>*/}
             {/*                               <p>Our entire project is open source, allowing for other people to add other functionality, and to help maintain our project. This allows us to directly interact with our users, get bug reports, and new features directly with our project.</p>*/}
             {/*                           </div>*/}
             {/*                       </div>*/}
             {/*                   </div>*/}
             {/*               </div>*/}
             {/*           </div>*/}
             {/*       </div>*/}
             {/*   </section>*/}
                {/*/!* Services Section End *!/*/}
                {/*/!* Counter Section Begin *!/*/}
                {/*<section className="counter">*/}
                {/*    <div className="container">*/}
                {/*        <div className="counter__content">*/}
                {/*            <div className="row">*/}
                {/*                <div className="col-lg-3 col-md-6 col-sm-6">*/}
                {/*                    <div className="counter__item">*/}
                {/*                        <div className="counter__item__text">*/}
                {/*                            <img src="img/icons/ci-1.png" alt="" />*/}
                {/*                            <h2 className="counter_num">20</h2>*/}
                {/*                            <p>songs discovered</p>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-3 col-md-6 col-sm-6">*/}
                {/*                    <div className="counter__item second__item">*/}
                {/*                        <div className="counter__item__text">*/}
                {/*                            <img src="img/icons/ci-2.png" alt="" />*/}
                {/*                            <h2 className="counter_num">4</h2>*/}
                {/*                            <p>artists accepted</p>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-3 col-md-6 col-sm-6">*/}
                {/*                    <div className="counter__item third__item">*/}
                {/*                        <div className="counter__item__text">*/}
                {/*                            <img src="img/icons/ci-3.png" alt="" />*/}
                {/*                            <h2 className="counter_num">5</h2>*/}
                {/*                            <p>amount of genres</p>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-3 col-md-6 col-sm-6">*/}
                {/*                    <div className="counter__item four__item">*/}
                {/*                        <div className="counter__item__text">*/}
                {/*                            <img src="img/icons/ci-4.png" alt="" />*/}
                {/*                            <h2 className="counter_num">23</h2>*/}
                {/*                            <p>songs suggested</p>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</section>*/}
                {/*/!* Counter Section End *!/*/}
                {/*/!* Team Section Begin *!/*/}
                {/*<section className="team spad set-bg" data-setbg="img/team-bg.jpg">*/}
                {/*    <div className="container">*/}
                {/*        <div className="row">*/}
                {/*            <div className="col-lg-12">*/}
                {/*                <div className="section-title team__title">*/}
                {/*                    <span>Nice to meet</span>*/}
                {/*                    <h2>OUR Team</h2>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*        <div className="row">*/}
                {/*            <div className="col-lg-3 col-md-6 col-sm-6 p-0">*/}
                {/*                <div className="team__item set-bg" data-setbg="img/team/team-1.jpg">*/}
                {/*                    <div className="team__item__text">*/}
                {/*                        <h4>Dhanish N</h4>*/}
                {/*                        <p>backend</p>*/}
                {/*                        <div className="team__item__social">*/}
                {/*                            <a href="#"><i className="fa fa-facebook" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-twitter" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-dribbble" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-instagram" /></a>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*            <div className="col-lg-3 col-md-6 col-sm-6 p-0">*/}
                {/*                <div className="team__item team__item--second set-bg" data-setbg="img/team/team-2.jpg">*/}
                {/*                    <div className="team__item__text">*/}
                {/*                        <h4>Niranjan M.</h4>*/}
                {/*                        <p>front end</p>*/}
                {/*                        <div className="team__item__social">*/}
                {/*                            <a href="#"><i className="fa fa-facebook" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-twitter" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-dribbble" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-instagram" /></a>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*            <div className="col-lg-3 col-md-6 col-sm-6 p-0">*/}
                {/*                <div className="team__item team__item--third set-bg" data-setbg="img/team/team-3.jpg">*/}
                {/*                    <div className="team__item__text">*/}
                {/*                        <h4>Charan B.</h4>*/}
                {/*                        <p>backend</p>*/}
                {/*                        <div className="team__item__social">*/}
                {/*                            <a href="#"><i className="fa fa-facebook" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-twitter" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-dribbble" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-instagram" /></a>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*            <div className="col-lg-3 col-md-6 col-sm-6 p-0">*/}
                {/*                <div className="team__item team__item--four set-bg" data-setbg="img/team/team-4.jpg">*/}
                {/*                    <div className="team__item__text">*/}
                {/*                        <h4>Leo X.</h4>*/}
                {/*                        <p>backend</p>*/}
                {/*                        <div className="team__item__social">*/}
                {/*                            <a href="#"><i className="fa fa-facebook" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-twitter" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-dribbble" /></a>*/}
                {/*                            <a href="#"><i className="fa fa-instagram" /></a>*/}
                {/*                        </div>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*            <div className="col-lg-12 p-0">*/}
                {/*                <div className="team__btn">*/}
                {/*                    <a href="#" className="primary-btn">Meet Our Team</a>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</section>*/}
                {/*/!* Team Section End *!/*/}
                {/*/!* Latest Blog Section Begin *!/*/}
                {/*<section className="latest spad">*/}
                {/*    <div className="container">*/}
                {/*        <div className="row">*/}
                {/*            <div className="col-lg-12">*/}
                {/*                <div className="section-title center-title">*/}
                {/*                    <span>Our Blog</span>*/}
                {/*                    <h2>Blog Update</h2>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*        <div className="row">*/}
                {/*            <div className="latest__slider owl-carousel">*/}
                {/*                <div className="col-lg-4">*/}
                {/*                    <div className="blog__item latest__item">*/}
                {/*                        <h4>What Makes Users Want to Share a Video on Social Media?</h4>*/}
                {/*                        <ul>*/}
                {/*                            <li>Jan 03, 2020</li>*/}
                {/*                            <li>05 Comment</li>*/}
                {/*                        </ul>*/}
                {/*                        <p>We recently launched a new website for a Vital client and wanted to share some of the*/}
                {/*                            cool features we were able...</p>*/}
                {/*                        <a href="#">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-4">*/}
                {/*                    <div className="blog__item latest__item">*/}
                {/*                        <h4>Bumper Ads: How to Tell a Story in 6 Seconds</h4>*/}
                {/*                        <ul>*/}
                {/*                            <li>Jan 03, 2020</li>*/}
                {/*                            <li>05 Comment</li>*/}
                {/*                        </ul>*/}
                {/*                        <p>We recently launched a new website for a Vital client and wanted to share some of the*/}
                {/*                            cool features we were able...</p>*/}
                {/*                        <a href="#">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-4">*/}
                {/*                    <div className="blog__item latest__item">*/}
                {/*                        <h4>What Makes Users Want to Share a Video on Social Media?</h4>*/}
                {/*                        <ul>*/}
                {/*                            <li>Jan 03, 2020</li>*/}
                {/*                            <li>05 Comment</li>*/}
                {/*                        </ul>*/}
                {/*                        <p>We recently launched a new website for a Vital client and wanted to share some of the*/}
                {/*                            cool features we were able...</p>*/}
                {/*                        <a href="#">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-4">*/}
                {/*                    <div className="blog__item latest__item">*/}
                {/*                        <h4>Bumper Ads: How to Tell a Story in 6 Seconds</h4>*/}
                {/*                        <ul>*/}
                {/*                            <li>Jan 03, 2020</li>*/}
                {/*                            <li>05 Comment</li>*/}
                {/*                        </ul>*/}
                {/*                        <p>We recently launched a new website for a Vital client and wanted to share some of the*/}
                {/*                            cool features we were able...</p>*/}
                {/*                        <a href="#">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-4">*/}
                {/*                    <div className="blog__item latest__item">*/}
                {/*                        <h4>What Makes Users Want to Share a Video on Social Media?</h4>*/}
                {/*                        <ul>*/}
                {/*                            <li>Jan 03, 2020</li>*/}
                {/*                            <li>05 Comment</li>*/}
                {/*                        </ul>*/}
                {/*                        <p>We recently launched a new website for a Vital client and wanted to share some of the*/}
                {/*                            cool features we were able...</p>*/}
                {/*                        <a href="#">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-4">*/}
                {/*                    <div className="blog__item latest__item">*/}
                {/*                        <h4>What Makes Users Want to Share a Video on Social Media?</h4>*/}
                {/*                        <ul>*/}
                {/*                            <li>Jan 03, 2020</li>*/}
                {/*                            <li>05 Comment</li>*/}
                {/*                        </ul>*/}
                {/*                        <p>We recently launched a new website for a Vital client and wanted to share some of the*/}
                {/*                            cool features we were able...</p>*/}
                {/*                        <a href="#">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-4">*/}
                {/*                    <div className="blog__item latest__item">*/}
                {/*                        <h4>What Makes Users Want to Share a Video on Social Media?</h4>*/}
                {/*                        <ul>*/}
                {/*                            <li>Jan 03, 2020</li>*/}
                {/*                            <li>05 Comment</li>*/}
                {/*                        </ul>*/}
                {/*                        <p>We recently launched a new website for a Vital client and wanted to share some of the*/}
                {/*                            cool features we were able...</p>*/}
                {/*                        <a href="#">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</section>*/}
                {/*/!* Latest Blog Section End *!/*/}
                {/*/!* Call To Action Section Begin *!/*/}
                {/*<section className="callto spad set-bg" data-setbg="img/callto-bg.jpg">*/}
                {/*    <div className="container">*/}
                {/*        <div className="row">*/}
                {/*            <div className="col-lg-8">*/}
                {/*                <div className="callto__text">*/}
                {/*                    <h2>Fresh Ideas, Fresh Moments Giving Wings to your Stories.</h2>*/}
                {/*                    <p>INC5000, Best places to work 2019</p>*/}
                {/*                    <a href="#">Start your stories</a>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</section>*/}
                {/*/!* Call To Action Section End *!/*/}
                {/*/!* Footer Section Begin *!/*/}
                {/*<footer className="footer">*/}
                {/*    <div className="container">*/}
                {/*        <div className="footer__top">*/}
                {/*            <div className="row">*/}
                {/*                <div className="col-lg-6 col-md-6">*/}
                {/*                    <div className="footer__top__logo">*/}
                {/*                        <a href="#"><img src="img/blah.png" alt="" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-6 col-md-6">*/}
                {/*                    <div className="footer__top__social">*/}
                {/*                        <a href="#"><i className="fa fa-facebook" /></a>*/}
                {/*                        <a href="#"><i className="fa fa-twitter" /></a>*/}
                {/*                        <a href="#"><i className="fa fa-dribbble" /></a>*/}
                {/*                        <a href="#"><i className="fa fa-instagram" /></a>*/}
                {/*                        <a href="#"><i className="fa fa-youtube-play" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*        <div className="footer__option">*/}
                {/*            <div className="row">*/}
                {/*                <div className="col-lg-4 col-md-6 col-sm-6">*/}
                {/*                    <div className="footer__option__item">*/}
                {/*                        <h5>About us</h5>*/}
                {/*                        <p>Formed in 2020 by Dhanish, Niranjan, Charan, and Leo, Spotlight is an open source website made to recommend people music by small artists that would otherwise never have the chance to grow. </p>*/}
                {/*                        <a href="/about" className="read__more">Read more <span className="arrow_right" /></a>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-2 col-md-3 col-sm-3">*/}
                {/*                    <div className="footer__option__item">*/}
                {/*                        <h5>Who we are</h5>*/}
                {/*                        <ul>*/}
                {/*                            <li><a href="#">Team</a></li>*/}
                {/*                            <li><a href="#">Carrers</a></li>*/}
                {/*                            <li><a href="#">Contact us</a></li>*/}
                {/*                            <li><a href="#">Locations</a></li>*/}
                {/*                        </ul>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-2 col-md-3 col-sm-3">*/}
                {/*                    <div className="footer__option__item">*/}
                {/*                        <h5>Our work</h5>*/}
                {/*                        <ul>*/}
                {/*                            <li><a href="#">Feature</a></li>*/}
                {/*                            <li><a href="#">Latest</a></li>*/}
                {/*                            <li><a href="#">Browse Archive</a></li>*/}
                {/*                            <li><a href="#">Video for web</a></li>*/}
                {/*                        </ul>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*                <div className="col-lg-4 col-md-12">*/}
                {/*                    <div className="footer__option__item">*/}
                {/*                        <h5>Newsletter</h5>*/}
                {/*                        <p>Videoprah is an award-winning, full-service production company specializing.</p>*/}
                {/*                        <form action="#">*/}
                {/*                            <input type="text" placeholder="Email" />*/}
                {/*                            <button type="submit"><i className="fa fa-send" /></button>*/}
                {/*                        </form>*/}
                {/*                    </div>*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*        <div className="footer__copyright">*/}
                {/*            <div className="row">*/}
                {/*                <div className="col-lg-12 text-center">*/}
                {/*                    /!* Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. *!/*/}
                {/*                    <p className="footer__copyright__text">Copyright ©*/}
                {/*                        All rights reserved | This template is made with <i className="fa fa-heart-o" aria-hidden="true" /> by <a href="https://colorlib.com" target="_blank">Colorlib</a>*/}
                {/*                    </p>*/}
                {/*                    /!* Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. *!/*/}
                {/*                </div>*/}
                {/*            </div>*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</footer>*/}
                {/* Footer Section End */}
            </>
        );
    }




//
// import Page from "./home.html";
// // export default Home;
// var template = { __html: Page};
//
// function Home(){
//     return (
//         <div dangerouslySetInnerHTML={template} />
//
//     );
// }
export default Home;

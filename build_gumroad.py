# Builds docs/gumroad/index.html. Works on Python 3.8+ (separate from build.py, which needs 3.12+).
from pathlib import Path
root = Path(__file__).parent / 'docs' / 'gumroad'
root.mkdir(parents=True, exist_ok=True)
B = '/susie-portfolio/gumroad/'
IMG = B + 'img/'

PAGE = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#321c2d"><link rel="stylesheet" href="/susie-portfolio/style.css">
<title>Susie Kirchgessner — Character-driven storyteller in image and text</title>
<meta name="description" content="Susie Kirchgessner makes character-driven wall art and fiction: Literary Legends, The Well Read Collection, and Mabel's Magical Morsels.">
<style>
.g-hero{padding-top:72px;padding-bottom:56px}
.g-hero h1{font-size:clamp(48px,7vw,104px);letter-spacing:-.05em;margin:24px 0 0}
.g-hero h1 em{color:var(--berry)}
.g-lead{font-family:Georgia,serif;font-size:clamp(21px,2.2vw,29px);line-height:1.4;letter-spacing:-.015em;max-width:820px;margin:30px 0 0}
.g-sub{color:var(--muted);max-width:720px;margin:20px 0 0}
.g-sec{padding:88px 0}
.g-sec.alt{background:var(--cream)}
.g-sec h2{font-size:clamp(36px,4.6vw,62px);letter-spacing:-.04em;margin:12px 0 22px}
.g-sec h3{font:500 24px/1.2 'Playfair Display',Georgia,serif;margin:44px 0 12px}
.g-copy{max-width:720px;color:var(--ink)}
.g-copy p{margin-bottom:16px}
.g-muted{color:var(--muted)}
.g-how{background:var(--plum);color:var(--paper);padding:64px 0}
.g-how .overline{color:#d4aebb}
.g-how h2{font-size:clamp(30px,3.6vw,46px);letter-spacing:-.03em;margin:12px 0 18px}
.g-how p{max-width:760px;color:#efe6ea;margin-bottom:14px}
.g-arc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin:36px 0 8px}
.g-arc figure{margin:0}
.g-arc img,.g-grid img,.g-wide img{display:block;width:100%;height:auto;background:#e9e2e0}
.g-arc figcaption,.g-grid figcaption,.g-wide figcaption{font-size:13px;color:var(--muted);margin-top:10px;line-height:1.45}
.g-arc figcaption b{display:block;color:var(--berry);font-size:11px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:3px}
.g-tag{font:italic 500 clamp(24px,3vw,38px)/1.2 'Playfair Display',Georgia,serif;color:var(--berry);margin:22px 0 0}
.g-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin:26px 0}
.g-grid.three{grid-template-columns:repeat(3,minmax(0,1fr))}
.g-grid figure,.g-wide{margin:0}
.g-wide{margin:26px 0}
.g-steps{list-style:none;padding:0;margin:14px 0 0;max-width:720px;border-top:1px solid var(--line)}
.g-steps li{padding:12px 0;border-bottom:1px solid var(--line)}
.g-steps b{font-family:'Playfair Display',Georgia,serif;font-weight:500;margin-right:6px}
.g-ex{margin:24px 0 8px;max-width:760px;background:var(--paper);border-left:3px solid var(--mauve);padding:22px 26px}
.g-ex p{font-family:Georgia,serif;font-size:17px;line-height:1.6;margin-bottom:14px}
.g-ex p:last-child{margin-bottom:0}
.g-src{font-size:13px;color:var(--muted);margin:0 0 26px}
.g-src a{color:var(--berry);font-weight:600;border-bottom:1px solid var(--mauve)}
.g-two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:40px;margin-top:34px;align-items:start}
.g-story{border-top:2px solid var(--plum);padding-top:22px}
.g-story h3{margin-top:6px}
.g-kind{text-transform:uppercase;letter-spacing:.14em;font-size:11px;font-weight:700;color:var(--berry);margin-bottom:0}
.g-lead-in{color:var(--muted);margin-top:22px;margin-bottom:0}
.g-story .g-ex{margin-top:12px}
.g-links{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:22px}
.g-links a{font-weight:700;font-size:14px;color:var(--berry);border-bottom:1px solid var(--mauve)}
.g-contact{background:var(--plum);color:var(--paper);padding:84px 0}
.g-contact h2{font-size:clamp(36px,4.6vw,62px);letter-spacing:-.04em;margin:12px 0 18px}
.g-contact .overline{color:#d4aebb}
.g-contact p{max-width:640px;color:#efe6ea}
.g-contact a.big{display:inline-block;font:500 clamp(22px,3vw,34px) 'Playfair Display',Georgia,serif;border-bottom:1px solid #d4aebb;margin:10px 0 22px}
.g-contact .g-links a{color:#f0d8e2;border-color:#7a6875}
@media(max-width:900px){.g-two{grid-template-columns:1fr}}
@media(max-width:820px){.g-arc,.g-grid,.g-grid.three{grid-template-columns:1fr 1fr}.g-arc{grid-template-columns:1fr}.site-header nav{display:none}}
@media(max-width:520px){.g-grid,.g-grid.three{grid-template-columns:1fr}}
</style></head><body>
<header class="site-header"><a class="wordmark" href="/susie-portfolio/gumroad/">S<span class="slash">/</span>K<span class="wordmark-full"> Susie Kirchgessner</span></a><nav aria-label="Main navigation"><a href="#legends">Literary Legends</a><a href="#wellread">Well Read</a><a href="#writing">Fiction</a><a href="#contact">Contact</a></nav></header>
<main>

<section class="g-hero wrap">
<div class="eyebrow"><span class="line"></span> Portfolio for Gumroad Creators in Residence</div>
<h1>Susie<br><em>Kirchgessner.</em></h1>
<p class="g-lead">I’m a character-driven storyteller who works in image and text. I take a character and their emotional arc and turn it into art for your wall or a story you can get lost in.</p>
<p class="g-sub">Three things I make: gothic literary wall art (<a href="#legends" class="text-link"><u>Literary Legends</u></a>), skeleton-and-books wall art (<a href="#wellread" class="text-link"><u>The Well Read Collection</u></a>), and fiction, which I publish as Sutton Krowley (<a href="#writing" class="text-link"><u>a cozy comedy and a romance</u></a>).</p>
</section>

<section class="g-how"><div class="wrap">
<p class="overline">How I make things</p>
<h2>I’ll say the AI part first.</h2>
<p>I can’t draw or paint by hand. What I’m good at is digital work and direction: knowing what I want, describing it in obsessive detail, and steering it through a lot of rounds until it’s right. I use AI tools to get ideas out of my gray matter noodle and into the world, and it’s given me far more creative freedom than I’d have without them.</p>
<p>I know some people have strong feelings about AI, so I’d rather just be upfront about how I use it. The characters, collection concepts, quotes, fonts, layouts, world-building, story structure, and editing are mine. You’ll find the exact steps under each project below.</p>
</div></section>

<section class="g-sec" id="legends"><div class="wrap">
<p class="overline">01 / Wall art</p>
<h2>Literary Legends</h2>
<div class="g-copy">
<p>Ten gothic, tragic “literary bad boys,” each one reimagined as double-exposure art. It started with a double-exposure animal sample I saw in Ideogram and the thought, <em>why not characters?</em> Then I was watching <em>The Last Voyage of the Demeter</em>, thinking about Frankenstein, and the list wouldn’t stop growing.</p>
<p>These are my own interpretations, not the famous film versions. Every piece comes with quotes pulled from the public-domain source text, so the character’s own words help tell the story.</p>
</div>

<h3>The arc: Erik, the Phantom of the Opera</h3>
<p class="g-muted g-copy">Each character gets a triptych. I curate three quotes that trace an emotional arc (past, present, future) and pick the typeface for each set, so you can see the font and feel the message. This is Erik’s “Heartache Arc,” built from Gaston Leroux’s original novel rather than the musical: grotesque, genius, and heartbreakingly human.</p>
<div class="g-arc">
<figure><img src="__IMG__erik-masked.jpg" alt="Erik the Phantom of the Opera, masked, in a dark gothic frame with a script quote" loading="lazy"><figcaption><b>Past</b>“Hideousness… Love had dared to face beauty.”</figcaption></figure>
<figure><img src="__IMG__erik-yearning.jpg" alt="Erik the Phantom of the Opera, yearning, in a dark gothic frame with a script quote" loading="lazy"><figcaption><b>Present</b>“All I ever needed was to be loved for myself.”</figcaption></figure>
<figure><img src="__IMG__erik-human.jpg" alt="Erik the Phantom of the Opera, human, in a dark gothic frame with a script quote" loading="lazy"><figcaption><b>Future</b>“I am not a bad man. Love me, you’ll see!”</figcaption></figure>
</div>
<p class="g-tag">Masked. Yearning. Human.</p>

<h3>More of the collection</h3>
<div class="g-grid">
<figure><img src="__IMG__dorian.jpg" alt="Dorian Gray, double-exposure portrait" loading="lazy"><figcaption>Dorian Gray</figcaption></figure>
<figure><img src="__IMG__heathcliff.jpg" alt="Heathcliff, double-exposure portrait" loading="lazy"><figcaption>Heathcliff</figcaption></figure>
<figure><img src="__IMG__ahab.jpg" alt="Captain Ahab, double-exposure portrait" loading="lazy"><figcaption>Captain Ahab</figcaption></figure>
<figure><img src="__IMG__frankenstein.jpg" alt="Frankenstein’s creature, double-exposure portrait" loading="lazy"><figcaption>The Creature (Frankenstein)</figcaption></figure>
</div>

<h3>How each one gets made</h3>
<ol class="g-steps">
<li><b>Concept.</b> I choose the character and curate imagery that matches the feel of the book.</li>
<li><b>Ideogram.</b> I generate the images and work the prompts through many, many rounds until each one feels right.</li>
<li><b>Photoshop.</b> I retouch for mood by hand, playing with filters and settings, then size everything for print.</li>
<li><b>Illustrator.</b> I choose the quotes and typeface, then build the layout and print ratios.</li>
</ol>
<div class="g-links"><a href="https://susiekirchdesigns.com/literary-legends-wall-art/" target="_blank" rel="noopener noreferrer">The full story of how it got built ↗</a><a href="https://www.etsy.com/shop/SusieKirchDesigns" target="_blank" rel="noopener noreferrer">The live Etsy shop ↗</a></div>
</div></section>

<section class="g-sec alt" id="wellread"><div class="wrap">
<p class="overline">02 / Wall art</p>
<h2>The Well Read Collection</h2>
<div class="g-copy">
<p>Skeletons, because who doesn’t love skeletons? The idea underneath is “dying to read,” a Halloween-type feel for the bookish world. It’s coordinating wall art you can mix by mood or season: <em>Dark Romance</em>, <em>Hearth</em>, <em>Library</em>, and <em>The Last Chapter</em>, a set of four.</p>
<p>I deliberately skipped phrase-based designs. I lean toward a watercolor look, and I spend a lot of time researching what’s already out there before I decide what’s worth making.</p>
</div>
<div class="g-wide"><img src="__IMG__wr-set.jpg" alt="The Last Chapter, a set of four skeleton-and-books prints in wooden frames on a wall" loading="lazy"><figcaption>The Last Chapter, a set of four</figcaption></div>
<div class="g-grid three" style="grid-template-columns:repeat(2,minmax(0,1fr))">
<figure><img src="__IMG__wr-dark-romance.jpg" alt="Dark Romance print, a gothic castle library scene, framed in a reading nook" loading="lazy"><figcaption>Dark Romance: a gothic castle library</figcaption></figure>
<figure><img src="__IMG__wr-nook.jpg" alt="A Well Read print framed above a cozy reading nook" loading="lazy"><figcaption>Well Read, in a reading nook</figcaption></figure>
</div>
<h3>How the pieces get made</h3>
<ol class="g-steps">
<li><b>Research.</b> Google Images and a lot of time on Etsy, studying what’s selling and what’s missing.</li>
<li><b>Exploring.</b> I started with Photoshop’s generative tools, wasn’t getting what I wanted, and took the prompt idea to Ideogram. The first four became The Last Chapter.</li>
<li><b>Building by mood.</b> Dark Romance, Hearth, Library, and a reading nook with a fireplace, grouped into one collection.</li>
<li><b>Photoshop.</b> Mood retouching with filters and settings, then sizing for print.</li>
</ol>
</div></section>

<section class="g-sec" id="writing"><div class="wrap">
<p class="overline">03 / Fiction</p>
<h2>Fiction</h2>
<div class="g-copy"><p>I write fiction as Sutton Krowley. Here are two stories in two very different moods, so you can see the range.</p></div>

<div class="g-two">
<article class="g-story">
<p class="g-kind">Cozy paranormal comedy · Web serial</p>
<h3>Mabel’s Magical Morsels</h3>
<p>A baker in Spellbound Springs, a town where the curses are more like guidelines than actual rules. The first ten chapters are live on Substack.</p>
<p class="g-lead-in">First, the tail end of a chapter with Gerald. Gerald is Gerald.</p>
<blockquote class="g-ex">
<p>“Of course not. Now, about our victory speech – I’ve prepared three versions. One dignified, one revolutionary, and one that may or may not involve the petit fours performing an interpretive dance to ‘Don’t Cry For Me, Mascarpone.’”</p>
<p>Mabel closed the recipe box with a snap. “We are not doing the mascarpone one.”</p>
<p>“We’ll revisit it,” Gerald said, already looking pleased with himself. “Democratically.”</p>
</blockquote>
<p class="g-src">From “Meet Gerald.” <a href="https://suttonkrowley.substack.com/p/meet-gerald" target="_blank" rel="noopener noreferrer">Read the chapter ↗</a></p>
<p class="g-lead-in">And the moment Mabel discovers the baked goods have opinions:</p>
<blockquote class="g-ex">
<p>To her astonishment, the baguettes were arguing. In French.</p>
<p>“Non, non, non!” one baguette exclaimed. “You cannot possibly suggest that butter is superior to olive oil! It’s a disgrace to our crusty heritage!”</p>
<p>“Oh, please,” another retorted, its crust crackling with indignation. “Your obsession with butter is making you soft. Olive oil is clearly the healthier choice!”</p>
<p>A third baguette chimed in, “Who cares about health? We’re bread! Our purpose is to be devoured by humans. The real question is: to be sliced or torn?”</p>
<p>“Sliced?!” gasped the first baguette. “You might as well suggest we throw ourselves into the toaster! No self-respecting baguette would allow itself to be sliced!”</p>
<p>“Speak for yourself,” a particularly crusty specimen drawled. “Some of us enjoy a little pain.”</p>
</blockquote>
<p class="g-src">From “A Spellbound Soufflé.” <a href="https://suttonkrowley.substack.com/p/a-spellbound-souffle" target="_blank" rel="noopener noreferrer">Read the chapter ↗</a></p>
</article>

<article class="g-story">
<p class="g-kind">Romance · Dual POV · Work in progress</p>
<h3>Meta Vertical Romance (MVR)</h3>
<p>A romance told in dual POV by Ainsley, a romance author, and Silas. This is Ainsley, in a bookstore, drifting toward the classics. (Trimmed with […] for length.)</p>
<blockquote class="g-ex">
<p>And then the classics.</p>
<p>I don’t know who I think I’m fooling. I always end up in the classics. Every bookstore, every city, every version of me that has ever stood in front of a wall of old spines — I end up here. Running my fingers along them like I’m checking for something. Like there’s a pulse.</p>
<p>Darcy first, because there’s always Darcy. The blueprint. The man who got it spectacularly wrong, admitted it in a letter, and then just — fixed himself. Quietly. Without fanfare. Came back better.</p>
<p>[…]</p>
<p>Heathcliff and Catherine. I paused. I always pause here. This is not a love story. This is a horror story that never got around to announcing itself, and somehow everyone treated it like a template anyway.</p>
<p>[…]</p>
<p>Rochester and Jane. That was the one that snagged.</p>
<p>Jane got to choose. That’s what I keep coming back to, the part I can’t quite put down: she looked at the wrong version of herself — the version that stayed, the version that bent — and she said <em>no</em> and she walked, and eventually she got to come back on her own terms. She made a choice. She had that.</p>
<p>My hand found the spine before I’d made any decision about it.</p>
<p>The thing about sudden loss is that there’s no chapter break. No moment where the narrative pauses and gives you room. It just happens. Like weather. Like something that isn’t in the story and then is, permanently, without your input, without your consent, in one clean terrible second.</p>
<p>I hadn’t gotten a choice. I’d just gotten an after.</p>
</blockquote>
<p class="g-src">From Chapter 2 of a work in progress.</p>
</article>
</div>

<h3>Building the worlds</h3>
<div class="g-copy">
<p>Both stories start with structure. Mabel’s world runs on a story bible I built in Notion: lore, magic systems, factions, beings, locations, a full cast, and a “Decision Graveyard” for ideas I killed on purpose. The magic has rules. It’s inherited, relational, and alive, and it runs on a “cozy covenant.” There’s a sneeze rule. And the chaos scales with Mabel’s emotional state: <em>calm Mabel = manageable magic; stressed Mabel = revolutionary dinner rolls.</em></p>
<p>MVR runs on a chapter database that tracks whose POV each chapter is in, the setting, the problem, and what changes by the end of it.</p>
<p>The ridiculous stuff only works if the world itself makes sense, so I build the rules first.</p>
</div>

<h3>How the writing gets made</h3>
<div class="g-copy">
<p>Same honesty as above: these stories are AI-assisted. I build the characters, structure, and beats; AI drafts from my direction; I edit, rework, and decide what stays. The voice, the world, and what actually makes it onto the page are mine to decide.</p>
</div>
</div></section>

<section class="g-contact" id="contact"><div class="wrap">
<p class="overline">04 / Say hello</p>
<h2>Thanks for looking.</h2>
<p>The shop, the blog, and the serial are all below. If you want to know how any of this got made, just ask.</p>
<a class="big" href="mailto:susie@susiekirchdesigns.com">susie@susiekirchdesigns.com ↗</a>
<div class="g-links">
<a href="https://www.etsy.com/shop/SusieKirchDesigns" target="_blank" rel="noopener noreferrer">Etsy shop ↗</a>
<a href="https://susiekirchdesigns.com/" target="_blank" rel="noopener noreferrer">Susie Kirch Designs ↗</a>
<a href="https://suttonkrowley.substack.com/" target="_blank" rel="noopener noreferrer">Sutton Krowley on Substack ↗</a>
<a href="/susie-portfolio/">Full portfolio ↗</a>
</div>
</div></section>

</main>
<footer><span>Susie Kirchgessner</span><span>Wall art · Fiction · Character-driven work</span><a href="mailto:susie@susiekirchdesigns.com">Get in touch ↗</a></footer>
</body></html>'''

(root / 'index.html').write_text(PAGE.replace('__IMG__', IMG), encoding='utf-8')
print('wrote', root / 'index.html')

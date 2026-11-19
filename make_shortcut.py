# ../recipe_button/recipe_bookmarklet.js から iPhone用の設定ページ（shortcut.html）を作る
# 使い方: py -3 make_shortcut.py
import io, os, html

here = os.path.dirname(os.path.abspath(__file__))
code = io.open(os.path.join(here, '..', 'recipe_button', 'recipe_bookmarklet.js'), encoding='utf-8').read()

page = '''<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>レシピ抜き出しの設定</title>
<link rel="apple-touch-icon" href="icon-180.png">
<style>
:root{--bg:#fbf6ee;--card:#fffdf9;--ink:#2b2520;--sub:#6f655a;--line:#e6dccd;--accent:#b8501c;--accent-ink:#fff;--soft:#f5e7d8;--ok:#2f7a4a;--warn:#8a5a00;--warn-soft:#fbf0d3;
--sans:"Hiragino Sans","Noto Sans JP","Yu Gothic UI","Meiryo UI",sans-serif;--mincho:"Hiragino Mincho ProN","Noto Serif JP","Yu Mincho",serif}
@media (prefers-color-scheme:dark){:root{--bg:#1d1a16;--card:#27231e;--ink:#f1eae0;--sub:#b3a898;--line:#3d372f;--accent:#e98a54;--accent-ink:#231305;--soft:#3a2c20;--ok:#7fd19c;--warn:#e8c26e;--warn-soft:#3a2f17}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.7;font-size:16px}
main{max-width:680px;margin:0 auto;padding:calc(16px + env(safe-area-inset-top)) 16px calc(32px + env(safe-area-inset-bottom))}
a{color:var(--accent)}
h1{font-family:var(--mincho);font-size:24px;line-height:1.35;margin:8px 0 6px}
.lead{color:var(--sub);margin:0 0 20px}
section{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;margin-bottom:12px}
h2{font-size:16px;margin:0 0 8px;color:var(--accent)}
ol{margin:0;padding-left:1.4em}li{margin:6px 0}
b.ui{background:var(--soft);border-radius:5px;padding:0 5px;font-weight:600}
.btn{display:flex;align-items:center;justify-content:center;width:100%;min-height:52px;border:0;border-radius:12px;background:var(--accent);color:var(--accent-ink);font:inherit;font-weight:700;margin:10px 0 4px;cursor:pointer}
#st{min-height:1.5em;font-weight:600;color:var(--ok);font-size:14px}
textarea{width:100%;height:84px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--sub);font:12px/1.4 monospace;padding:8px}
.note{color:var(--sub);font-size:14px}
.warn{background:var(--warn-soft);color:var(--warn);border-radius:10px;padding:10px 12px;font-size:14px;margin-top:10px}
</style></head><body><main>
<a href="./index.html">‹ レシピアプリへ</a>
<h1>レシピ抜き出しの設定</h1>
<p class="lead">Safariで見ているレシピを、共有ボタンから抜き出してコピーできるようにします。最初に1回だけ、iPhoneのショートカットを作ります。</p>

<section><h2>1. スクリプトを許可する</h2>
<p style="margin:0">iPhoneの<b class="ui">設定</b> → <b class="ui">アプリ</b> → <b class="ui">ショートカット</b> → <b class="ui">詳細</b> と進み、<b class="ui">スクリプトの実行を許可</b>をオンにします。</p>
<p class="note" style="margin:6px 0 0">iOSが古いときは、<b class="ui">設定</b> → <b class="ui">ショートカット</b> → <b class="ui">詳細</b> です。</p></section>

<section><h2>2. 中身をコピーする</h2>
<button class="btn" id="copy">抜き出しの中身をコピー</button>
<div id="st" role="status"></div>
<textarea id="code" readonly aria-label="ショートカットに貼り付ける中身">__CODE__</textarea></section>

<section><h2>3. ショートカットを作る</h2>
<ol>
<li><b class="ui">ショートカット</b>アプリを開き、右上の<b class="ui">＋</b>を押す</li>
<li>検索欄に <b>JavaScript</b> と入れて、<b class="ui">WebページでJavaScriptを実行</b>を選ぶ</li>
<li>入っている例の文字を全部消して、長押しで<b class="ui">ペースト</b>する（2. でコピーした中身）</li>
<li>検索欄に <b>クリップボード</b> と入れて、<b class="ui">クリップボードにコピー</b>を選ぶ（中身は前の動作の結果のまま）</li>
<li>上の名前を<b>レシピ抜き出し</b>にする</li>
<li>名前の横のメニューか<b class="ui">ⓘ</b>から<b class="ui">共有シートに表示</b>をオンにして、受け取るものを<b class="ui">Safari Webページ</b>だけにする</li>
<li><b class="ui">完了</b>を押す</li>
</ol>
<p class="note" style="margin:8px 0 0">iOSのバージョンによって、ボタンの名前や場所が少し違うことがあります。</p></section>

<section><h2>4. 使い方</h2>
<ol>
<li>Safariでレシピのページを開き、<b class="ui">共有ボタン</b> → <b class="ui">レシピ抜き出し</b>を押す</li>
<li>初めてのサイトでは許可を聞かれるので、<b class="ui">許可</b>を押す</li>
<li>ページの上に内容が出て、全部がコピーされます。材料だけ欲しいときは、そこで<b class="ui">材料だけ</b>を押す</li>
<li>ホーム画面のレシピアプリで<b class="ui">＋追加</b> → <b class="ui">コピーした文字を読み込む</b> → <b class="ui">保存</b></li>
</ol>
<div class="warn">共有シートに出ないときは、一覧のいちばん下の<b>アクションを編集</b>から追加できます。</div></section>

<h1 id="shot" style="margin-top:28px">スクショから登録</h1>
<p class="lead">YouTubeやInstagramの画面のスクショから、iPhoneの文字認識で文字を読み取って登録します。読み取りはiPhoneの中で行われ、画像はどこにも送られません。</p>

<section><h2>1. ショートカットを作る（最初の1回だけ）</h2>
<ol>
<li><b class="ui">ショートカット</b>アプリで右上の<b class="ui">＋</b>を押す</li>
<li>検索欄に <b>繰り返す</b> と入れて、<b class="ui">各項目を繰り返す</b>を選ぶ（対象は「ショートカットの入力」）</li>
<li>検索欄に <b>テキストを抽出</b> と入れて、<b class="ui">画像からテキストを抽出</b>を選び、繰り返しの<b>中</b>に入れる（画像は「繰り返し項目」）</li>
<li>検索欄に <b>結合</b> と入れて、<b class="ui">テキストを結合</b>を選び、繰り返しの<b>後</b>に置く（「繰り返しの結果」を<b>改行</b>で結合）</li>
<li>続けて<b class="ui">クリップボードにコピー</b>を追加する</li>
<li>名前を<b>スクショの文字をコピー</b>にする</li>
<li><b class="ui">ⓘ</b>から<b class="ui">共有シートに表示</b>をオンにして、受け取るものを<b class="ui">イメージ</b>だけにする → <b class="ui">完了</b></li>
</ol>
<p class="note" style="margin:8px 0 0">「画像からテキストを抽出」は iOS 15 以降・iPhone XS 以降で使えます。</p></section>

<section><h2>2. 使い方</h2>
<ol>
<li>材料や作り方が映っている画面をスクショする（何枚でも）。YouTubeは説明欄、Instagramは本文や画像のレシピのページ</li>
<li><b class="ui">写真</b>アプリでそのスクショを選び（複数なら<b class="ui">選択</b>で順番に）、<b class="ui">共有ボタン</b> → <b class="ui">スクショの文字をコピー</b></li>
<li>レシピアプリで<b class="ui">＋追加</b> → <b class="ui">コピーした文字を読み込む</b></li>
<li>料理名・材料・作り方を確かめて直し、下の<b class="ui">写真を追加</b>で同じスクショを付けて<b class="ui">保存</b></li>
</ol>
<div class="warn">文字認識なので、読み違いや「いいね」などの画面の文字が混ざることがあります。保存の前に必ず目で確かめてください。スクショを写真として付けておけば、料理中も元の画面を見られます。</div></section>
</main>
<script>
document.getElementById('copy').addEventListener('click',function(){
  var t=document.getElementById('code'),st=document.getElementById('st');
  function ok(){st.textContent='✔ コピーしました。続けて 3. に進んでください';}
  function legacy(){t.focus();t.select();t.setSelectionRange(0,t.value.length);
    var r=false;try{r=document.execCommand('copy');}catch(e){}
    if(r)ok();else st.textContent='コピーできませんでした。下の文字を長押しして全部選択し、コピーしてください';}
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(t.value).then(ok,legacy);else legacy();
});
</script>
</body></html>
'''
page = page.replace('__CODE__', html.escape(code))
io.open(os.path.join(here, 'shortcut.html'), 'w', encoding='utf-8', newline='\n').write(page)
print('ok', len(code))

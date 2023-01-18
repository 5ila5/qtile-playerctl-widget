Playerctl
=========
```python
class libqtile.widget.Playerctl(*args, **kwargs)
```

   Supported bar orientations: horizontal only

   **Configuration options**

  <table class="docutils align-default">

<thead>
<tr class="row-odd"><th class="head"><p>key</p></th>
<th class="head"><p>default</p></th>
<th class="head"><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">app_player_icons</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">{'spotifyd':</span> <span class="pre">'spotify'}</span></code></p></td>
<td><p>Replaces Icon of first_app with the second Default: replaces Spotifyd(not found) icon with spotify Icon (if installed)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">background</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">None</span></code></p></td>
<td><p>Widget background color</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">bottom_margin</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">3</span></code></p></td>
<td><p>Distance between bottom of the Bar Icon</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">controll_multiple</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>shows Icon with the currently selected player if False Controlls always all Player at once</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">default_icon</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">'~/Pictures/not_found.png'</span></code></p></td>
<td><p>Default icon if no icon for the given Application found</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">distance</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">10</span></code></p></td>
<td><p>distance Betwen Icons distance multiplier*icon_width Play/Pause</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">fmt</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">'{}'</span></code></p></td>
<td><p>To format the string returned by the widget. For example, if the clock widget              returns '08:46' we can do fmt='time {}' do print 'time 08:46' on the widget.              To format the individual strings like hour and minutes use the format paramater              of the widget (if it has one)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">font</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">'sans'</span></code></p></td>
<td><p>Default font</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">fontshadow</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">None</span></code></p></td>
<td><p>font shadow color, default is None(no shadow)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">fontsize</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">None</span></code></p></td>
<td><p>Font size. Calculated if None.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">foreground</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">'ffffff'</span></code></p></td>
<td><p>Foreground colour</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">icon_color</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">'FFFFFF'</span></code></p></td>
<td><p>Color of Play Pause Next... Icons</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">icon_order</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">(1,</span> <span class="pre">2,</span> <span class="pre">3)</span></code></p></td>
<td><p>Order of Icons (1,2,3) represents prev -&gt; Pl/pause -&gt; next</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">icon_width</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">(20,</span> <span class="pre">30)</span></code></p></td>
<td><p>Width of Play/Pause(1) and Next/Pref(2) Buttons</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">list</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">[]</span></code></p></td>
<td><p>White Blacklist dependent on list_type. playerctl player name "all" Black/Whitelists the general Controll</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">list_type</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">0</span></code></p></td>
<td><p>0 all Applications, 1 Blacklist,2 Whitelist</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">markup</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>Whether or not to use pango markup</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">max_chars</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">0</span></code></p></td>
<td><p>Maximum number of characters to display in widget.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">mouse_callbacks</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">{}</span></code></p></td>
<td><p>Dict of mouse button press callback functions. Accepts functions and <code class="docutils literal notranslate"><span class="pre">lazy</span></code> calls.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">padding</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">None</span></code></p></td>
<td><p>Padding. Calculated if None.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">player_icons</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">{}</span></code></p></td>
<td><p>path to icons format {"player_name": "source to icon"}</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">scroll</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">False</span></code></p></td>
<td><p>Whether text should be scrolled. When True, you must set the widget's <code class="docutils literal notranslate"><span class="pre">width</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">scroll_clear</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">False</span></code></p></td>
<td><p>Whether text should scroll completely away (True) or stop when the end of the text is shown (False)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">scroll_delay</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">2</span></code></p></td>
<td><p>Number of seconds to pause before starting scrolling and restarting/clearing text at end</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">scroll_hide</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">False</span></code></p></td>
<td><p>Whether the widget should hide when scrolling has finished</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">scroll_interval</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">0.1</span></code></p></td>
<td><p>Time in seconds before next scrolling step</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">scroll_repeat</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>Whether text should restart scrolling once the text has ended</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">scroll_step</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">1</span></code></p></td>
<td><p>Number of pixels to scroll with each step</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">showVolume</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>show Playervolume like the Volume Widget</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">show_next</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>Show next Track button</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">show_prev</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>Show previous Track button</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">top_margin</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">3</span></code></p></td>
<td><p>Distance between top of the Bar Icon</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">update_interval</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">0.5</span></code></p></td>
<td><p>Update time in seconds.</p></td>
</tr>
</tbody>
</table>
   

import spell
import spellbook

ratty_textbook = Spellbook("Paper", 5)


### Big example

tablet = Spellbook('Stone', 24)
post_it_note = Spellbook('Paper', 3)

tickle_effect = "You point at a target and watch them squirm as an invisible" \
        " feather begins tickling at their sides! Or not. Some people aren't" \
        " ticklish."
tickle = Spell('Tickle', 'Evocation', 0, 100, tickle_effect)

castle_effect = "You sing a showstopping Broadway tune and build an ice " \
        "castle out of basically nothing. That feels pretty great."
castle = Spell("Queen Elsa's Instant Castle", 'Transmutation', 8, 1,
        castle_effect)

cheesecake_effect = "You mutter a few words and a slice of cheesecake " \
        "spontaneously appears on a point that you can see within range. " \
        "Then two slices. Then four. Then eight. Sixteen. Thirty-two. Oh no..."
cheesecake = Spell("Cheesecake Calamity", 'Conjuration', 8, 5,
        cheesecake_effect)

anti_cheesecake_effect = "For the next five minutes, any continuous segment " \
        "of cheesecake you touch immediately disintegrates. It tastes lovely."
anti_cheesecake = Spell("Destroy Cheesecake", 'Evocation', 7, 3,
        anti_cheesecake_effect)

f_ball_effect = "You crush a bit of charcoal between your fingers and " \
        "specify a point within 120 feet. An explosion of heat and light " \
        "(and smoke!) expands from that point, and it's just SO PRETTY."
f_ball = Spell("Fireball", 'Evocation', 3, 3, f_ball_effect)

post_it_note.add_spell(tickle)
post_it_note.add_spell(f_ball)

try:
    post_it_note.add_spell(cheesecake)
except ValueError as e:
    print(e)

post_it_note.cast_spell("Destroy Cheesecake")
post_it_note.cast_spell("Fireball")
post_it_note.cast_all()

tablet.add_spell(summon)
tablet.add_spell(cheesecake)
tablet.add_spell(castle)
tablet.add_spell(anti_cheesecake)

tablet.cast_strongest() # This should cast "Elsa's Instant Castle"
tablet.cast_strongest() # This should cast "Cheesecake Calamity"

tablet.cast_all()
tablet.refresh_all()

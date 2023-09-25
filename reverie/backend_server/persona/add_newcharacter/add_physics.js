// *** SET UP PERSONAS ***
// We start by creating the game sprite objects.
for (let i=0; i<Object.keys(spawn_tile_loc).length; i++) {
    let persona_name = Object.keys(spawn_tile_loc)[i];
    let start_pos = [spawn_tile_loc[persona_name][0] * tile_width + tile_width / 2,
        spawn_tile_loc[persona_name][1] * tile_width + tile_width];
    let new_sprite = this.physics.add
        .sprite(start_pos[0], start_pos[1], persona_name, "down")
        .setSize(30, 40)
        .setOffset(0, 0);
// Scale up the sprite
    new_sprite.displayWidth = 40;
    new_sprite.scaleY = new_sprite.scaleX;
}
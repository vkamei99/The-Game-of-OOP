from config_jogo import img,scale


sprite_isolde_andando = img(r'./imagens/sprite/isolde_andando.png')
sprite_isolde_atacando = img(r'./imagens/sprite/isolde_atacando.png')
sprite_isolde_especial = img(r'./imagens/sprite/isolde_especial.png')
sprite_isolde_rosto = img(r'./imagens/sprite/isolde_rosto.png')
sprite_isolde_rosto_especial = img(r'./imagens/sprite/isolde_rosto_especial.png')
sprites_isolde = (sprite_isolde_andando, sprite_isolde_atacando, sprite_isolde_especial, sprite_isolde_rosto, sprite_isolde_rosto_especial)

sprite_pitbull_andando = img(r'./imagens/sprite/pitbull_andando.png')
sprite_pitbull_atacando = img(r'./imagens/sprite/pitbull_atacando.png')
sprite_pitbull_especial = img(r'./imagens/sprite/pitbull_especial.png')
sprite_pitbull_rosto = img(r'./imagens/sprite/pitbull_rosto.png')
sprite_pitbull_rosto_especial = img(r'./imagens/sprite/pitbull_rosto_especial.png')
sprites_pitbull = (sprite_pitbull_andando, sprite_pitbull_atacando, sprite_pitbull_especial, sprite_pitbull_rosto, sprite_pitbull_rosto_especial)

sprite_lacertus_andando = img(r'./imagens/sprite/lacertus_andando.png')
sprite_lacertus_atacando = img(r'./imagens/sprite/lacertus_atacando.png')
sprite_lacertus_especial = img(r'./imagens/sprite/lacertus_especial.png')
sprite_lacertus_rosto = img(r'./imagens/sprite/lacertus_rosto.png')
sprite_lacertus_rosto_especial = img(r'./imagens/sprite/lacertus_rosto_especial.png')
sprite_lacertus_magia = scale(img(r'./imagens/sprite/lacertus_magia.png'), 0.03)
sprite_lacertus_ataque_especial = img(r'./imagens/sprite/lacertus_ataque_especial.png')
sprites_lacertus = (sprite_lacertus_andando, sprite_lacertus_atacando,sprite_lacertus_especial, sprite_lacertus_rosto, sprite_lacertus_rosto_especial,sprite_lacertus_magia, sprite_lacertus_ataque_especial)

sprite_draco_andando = img(r'./imagens/sprite/draco_andando.png')
sprite_draco_atacando= img(r'./imagens/sprite/draco_atacando.png')
sprite_draco_especial = img(r'./imagens/sprite/draco_especial.png')
sprite_draco_rosto= img(r'./imagens/sprite/draco_rosto.png')
sprite_draco_rosto_especial= img(r'./imagens/sprite/draco_rosto_especial.png')
sprite_draco_flecha= scale(img(r'./imagens/sprite/draco_flecha.png'), 0.2)
sprites_draco = (sprite_draco_andando, sprite_draco_atacando, sprite_draco_especial, sprite_draco_rosto, sprite_draco_rosto_especial,sprite_draco_flecha)

Lista_sprites = [sprites_isolde, sprites_pitbull, sprites_lacertus, sprites_draco]
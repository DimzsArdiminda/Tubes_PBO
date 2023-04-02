
                                        # # Render buttons
                                        # exit_text = ubuntuLight30.render("EXIT", 1, Game.COLOURS.get("whiteOutline"))
                                        # exit_rect = exit_text.get_rect(center=(cWidth/2, 220))
                                        # restart_text = ubuntuLight30.render("RESTART", 1, Game.COLOURS.get("whiteOutline"))
                                        # restart_rect = restart_text.get_rect(center=(cWidth/2, 180))

                                        # # Game state
                                        # score = 0
                                        # # TODO: Add other game state variables as needed

                                        # def restart_game():
                                        #     global score
                                        #      # TODO: Reset other game state variables as needed
                                        #     score = 0


                                        # # Game loop
                                        # running = True
                                        # while running:
                                        #     # Handle events
                                        #     for event in pygame.event.get():
                                        #         if event.type == pygame.QUIT:
                                        #             running = False
                                        #         elif event.type == pygame.MOUSEBUTTONUP:
                                        #             # Check if the mouse clicked on a button
                                        #             if exit_rect.collidepoint(event.pos):
                                        #                 running = False
                                        #             elif restart_rect.collidepoint(event.pos):
                                        #                 # Restart the game
                                        #                 restart_game()

                                        #     # Draw the buttons
                                        #     display.blit(exit_text, exit_rect)
                                        #     display.blit(restart_text, restart_rect)

                                        #     # Update the display
                                        #     pygame.display.update()

                                        #     # Quit pygame
                                        #     pygame.quit()


                                        # size = Button(cWidth/2 - 100, cHeight - 150, 200, 50, str(world.passengersMoved)+" Lives Saved", 30, Game.COLOURS.get("whiteOutline"), Game.COLOURS.get("button"))
                                        # size.draw(display)
                                        # for event in pygame.event.get():
                                        #     if event.type == pygame.MOUSEBUTTONDOWN:
                                        #         if size.is_clicked(pygame.mouse.get_pos()):
                                        #             # lakukan sesuatu di sini jika tombol diklik
                                        #             pygame.quit()  # keluar dari Pygame
                                        #             python = sys.executable
                                        #             os.execl(python, python, *sys.argv)  # jalankan ulang program Python

                                        # Game loop
                                        running = True
                                        while running:
                                            # Handle events
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    running = False
                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                    # Check if the mouse clicked on a button
                                                    if exit_rect.collidepoint(event.pos):
                                                        running = False
                                                    elif restart_rect.collidepoint(event.pos):
                                                        # Restart the game , masukin kode buat nge restart
                                                        StartMenu.run(self)
                                                        pass

                                            # Draw the buttons
                                            display.blit(exit_text, exit_rect)
                                            display.blit(restart_text, restart_rect)

                                            # Update the display
                                            pygame.display.update()

                                        # Quit pygame
                                        pygame.quit()
                
                                        # INI CUMA TEKS
                                        # size = ubuntuLight30.size(
                                        #     "REPLAY")
                                        # display.blit(ubuntuBold40.render("REPLAY",
                                        #                                 1,
                                        #                                 Game.COLOURS.get("whiteOutline")),
                                        #             (cWidth//2-size[0]//2,
                                        #             cHeight - 150))
                                        # size = ubuntuLight30.size(
                                        #     "QUIT")
                                        # display.blit(ubuntuBold40.render("QUIT",
                                        #                                 1,
                                        #                                 Game.COLOURS.get("whiteOutline")),
                                        #             (cWidth//2-size[0]//2,
                                        #             cHeight - 180))

                                        
                                        # for event in pygame.event.get():
                                        #     if event.type == pygame.MOUSEBUTTONDOWN:
                                        #         # Check if the replay button is clicked
                                        #         if replayButton.is_clicked(pygame.mouse.get_pos()):
                                        #             # Restart the game
                                        #             pygame.quit()
                                        #             python = sys.executable
                                        #             os.startfile(sys.executable)
                                        #             pygame.quit()
                                        #             sys.exit()

                                        #         # Check if the exit button is clicked
                                        #         elif exitButton.is_clicked(pygame.mouse.get_pos()):
                                        #             pygame.quit()
                                        #             sys.exit()
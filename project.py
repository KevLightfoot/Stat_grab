class Project:
    def __init__(self, matchup_array):
        self.array = matchup_array
        self.winners = []
        self.rankings = []

    def display_all_matchups(self):
        for matchup in self.array:
            matchup.display_matchup()

    def proj_score(self, p=True):
        for matchup in self.array:

            if matchup.ppg_diff.split("↑")[0].rstrip() != 0:
                sup_off = matchup.ppg_diff.split("↑")[0].rstrip()

            else:
                sup_off = 0
            if matchup.oppg_diff.split("↑")[0].rstrip() != 0:
                sup_def = matchup.oppg_diff.split("↑")[0].rstrip()
            else:
                sup_def = 0

            off_diff = matchup.ppg_diff.split("↑")[1]
            off_adv= off_diff.split("(")[0]
            off_adv = float(off_adv.strip())

            def_diff = matchup.oppg_diff.split("↑")[1]
            def_adv = def_diff.split("(")[0]
            def_adv = float(def_adv.strip())

            if sup_def == sup_off:
                adv = off_adv + def_adv
                team = sup_def
            elif off_adv > def_adv:
                adv = off_adv - def_adv
                team = sup_off
            elif def_adv > off_adv:
                adv = def_adv - off_adv
                team = sup_def
            else:
                team = 'error'
                adv = 0


            team1_proj_poss = (matchup.team1pospg[0] + matchup.team2pospg[0]) / 2
            team1_proj_points_per_poss = (matchup.team1eff_poss_ratio[0] + matchup.team2opp_eff_poss_ratio[0]) / 2
            team1_proj_points = round(team1_proj_poss * team1_proj_points_per_poss, 2)

            team2_proj_poss = (matchup.team2pospg[0] + matchup.team1pospg[0]) / 2
            team2_proj_points_per_poss = (matchup.team2eff_poss_ratio[0] + matchup.team1opp_eff_poss_ratio[0]) / 2
            team2_proj_points = round(team2_proj_poss * team2_proj_points_per_poss, 2)

            if p:
                if sup_def == sup_off:
                    adv = off_adv + def_adv
                    team = sup_def
                    print(f"Final Ranking: {team} ↑ {round(adv, 2)}")
                elif off_adv > def_adv:
                    adv = off_adv - def_adv
                    team = sup_off
                    print(f"Final Ranking: {team} ↑ {round(adv, 2)}")
                elif def_adv > off_adv:
                    adv = def_adv - off_adv
                    team = sup_off
                    print(f"Final Ranking: {team} ↑ {round(adv, 2)}")
                self.print_winner(team, adv)
            else:
                self.print_winner(team, adv, False)

    def print_winner(self, team, adv, p=True):

            winner_str = f"{team} by {round(adv, 2)}\n"
            if p:
                print(winner_str)
            self.winners.append((team, round(adv, 2)))

    def display_winners(self):
        print("\n\n\ndisplaying winners\n\n\n")
        print("\nWinners:")
        sorted_winners = sorted(self.winners, key=lambda x: x[1], reverse=True)
        for winner in sorted_winners:
            print(winner)
        reformatted_list = [item[0] for item in sorted_winners]
        print(reformatted_list)
from compare import compare

class analyze:
    def __init__(self, matchup_array):
        self.array = matchup_array
        self.winners = []
        self.rankings = []

    def display_all_matchups(self):
        for x in self.array:
            compare.display_matchup(self)

    def proj_score(self, p=True):
        for match in self.array:

            if match.ppg_diff.split("↑")[0].rstrip() != 0:
                sup_off = match.ppg_diff.split("↑")[0].rstrip()

            else:
                sup_off = 0
            if match.oppg_diff.split("↑")[0].rstrip() != 0:
                sup_def = match.oppg_diff.split("↑")[0].rstrip()
            else:
                sup_def = 0

            off_diff = match.ppg_diff.split("↑")[1]
            off_adv= off_diff.split("(")[0]
            off_adv = float(off_adv.strip())

            def_diff = match.oppg_diff.split("↑")[1]
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
        print("\nWinners:")
        sorted_winners = sorted(self.winners, key=lambda x: x[1], reverse=True)
        for winner in sorted_winners:
            print(winner)
        reformatted_list = [item[0] for item in sorted_winners]
        print(reformatted_list)

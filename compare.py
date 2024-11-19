class compare:
    def __init__(self, team1='', team2='', team1rank='', team2rank='', team1ppg='', team2ppg='',
                team1oppg='', team2oppg='', team1ypg='', team2ypg='', team1oypg='', team2_oypg='',
                team1_sos='', team2_sos='', team1_pyd='', team2_pyd='', team1_opyd='', team2_opyd='',
                team1_sacks_all='', team2_sacks_all='', team1_sacks='', team2_sacks='', team1_ryd='',
                team2_ryd='', team1_oryd='', team2_oryd='', team1_third_down='', team2_third_down='',
                team1_opp_third_down ='', team2_opp_third_down='', team1_redzone='', team2_redzone='',
                team1_redzone_d='', team2_redzone_d=''):

        self.team1 = team1
        self.team2 = team2
        self.team1rank = int(team1rank)
        self.team2rank = int(team2rank)
        self.rank_diff = ''
        self.team1ppg = team1ppg
        self.team2ppg = team2ppg
        self.ppg_diff = ''
        self.team1oppg = team1oppg
        self.team2oppg = team2oppg
        self.oppg_diff = ''
        self.team1ypg = team1ypg
        self.team2ypg = team2ypg
        self.ypg_diff = ''
        self.team1oypg = team1oypg
        self.team2_oypg = team2_oypg
        self.oypg_diff = ''
        self.team1_sos = team1_sos
        self.team2_sos = team2_sos
        self.sos_diff = ''
        self.team1_pyd = team1_pyd
        self.team2_pyd = team2_pyd
        self.pyd_diff = ''
        self.team1_opyd = team1_opyd
        self.team2_opyd = team2_opyd
        self.opyd_diff = ''
        self.team1_sacks_all = team1_sacks_all
        self.team2_sacks_all = team2_sacks_all
        self.sacks_all_diff = ''
        self.team1_sacks = team1_sacks
        self.team2_sacks = team2_sacks
        self.sacks_diff = ''
        self.team1_ryd = team1_ryd
        self.team2_ryd = team2_ryd
        self.ryd_diff = ''
        self.team1_oryd = team1_oryd
        self.team2_oryd = team2_oryd
        self.oryd_diff = ''
        self.team1_third_down = team1_third_down
        self.team2_third_down = team2_third_down
        self.third_down_diff = ''
        self.team1_third_down_d = team1_opp_third_down
        self.team2_third_down_d =team2_opp_third_down
        self.third_down_d_diff = ''
        self.team1_redzone = team1_redzone
        self.team2_redzone =team2_redzone
        self.redzone_diff = ''
        self.team1_redzone_d = team1_redzone_d
        self.team2_redzone_d = team2_redzone_d
        self.redzone_d_diff = ''






    def get_diff(self, stat):
        team1_stat = getattr(self, f'team1{stat}')
        team2_stat = getattr(self, f'team2{stat}')

        diff = team1_stat - team2_stat
        if diff > 0:
            diff = int(diff)

            print(f"\n{self.team2} \u2191 {diff}\n")

        else:
            diff = abs(diff)
            print(f"\n{self.team1} \u2191 {diff}\n")

        return f"\n{self.team1} \u2191 {diff}"

    def compare_stats(self, team1_stat, team2_stat, team1_rank, team2_rank, lower_is_better=False):
        rank_diff = team1_rank - team2_rank

        if lower_is_better:
            if team1_stat < team2_stat:
                diff = team2_stat - team1_stat
                print(f"{self.team1} ↑ {diff:.1f} ({abs(rank_diff)})\n")
                return f"{self.team1} ↑ {diff:.1f} ({abs(rank_diff)})\n"
            elif team2_stat < team1_stat:
                diff = team1_stat - team2_stat
                print(f"{self.team2} ↑ {diff:.1f} ({abs(rank_diff)})\n")
                return f"{self.team2} ↑ {diff:.1f} ({abs(rank_diff)})\n"
            else:
                diff = 0
        else:
            if team1_stat > team2_stat:
                diff = team1_stat - team2_stat
                print(f"{self.team1} ↑ {diff:.1f} ({abs(rank_diff)})\n")
                return f"{self.team1} ↑ {diff:.1f} ({abs(rank_diff)})\n"
            elif team2_stat > team1_stat:
                diff = team2_stat - team1_stat
                print(f"{self.team2} ↑ {diff:.1f} ({abs(rank_diff)})\n")
                return f"{self.team2} ↑ {diff:.1f} ({abs(rank_diff)})\n"
            else:
                diff = 0

        return f"{self.team2} ↑ {diff:.1f} ({abs(rank_diff)})"




    def display_matchup(self):
            # Print matchup
            print(f"#{self.team1rank} {self.team1} at #{self.team2rank} {self.team2}\n")



            # Print PPG
            print("Points Per Game:")
            print(f"{self.team1} : {self.team1ppg[0]:.1f} ({self.team1ppg[1]})")
            print(f"{self.team2} : {self.team2ppg[0]:.1f} ({self.team2ppg[1]})")
            # Compare PPG
            self.ppg_diff = self.compare_stats(self.team1ppg[0], self.team2ppg[0], self.team1ppg[1], self.team2ppg[1])

            # Print Opp PPG
            print("Opponent PPG:")
            print(f"{self.team1} : {self.team1oppg[0]:.1f} ({self.team1oppg[1]})")
            print(f"{self.team2} : {self.team2oppg[0]:.1f} ({self.team2oppg[1]})")
            # Compare PPG
            self.ppg_diff = self.compare_stats(self.team1oppg[0], self.team2oppg[0], self.team1oppg[1],
                                               self.team2oppg[1], lower_is_better=True)


            # Print YPG
            print("Yards Per Game:")
            print(f"{self.team1} : {self.team1ypg[0]:.1f} ({self.team1ypg[1]})")
            print(f"{self.team2} : {self.team2ypg[0]:.1f} ({self.team2ypg[1]})")
            # Compare YPG
            self.ypg_diff = self.compare_stats(self.team1ypg[0], self.team2ypg[0], self.team1ypg[1], self.team2ypg[1])

            # Print PYPG
            print("Passing Yards:")
            print(f"{self.team1} : {self.team1_pyd[0]:.1f} ({self.team1_pyd[1]})")
            print(f"{self.team2} : {self.team2_pyd[0]:.1f} ({self.team2_pyd[1]})")
            # Compare YPG
            self.pyd_diff = self.compare_stats(self.team1_pyd[0], self.team2_pyd[0], self.team1_pyd[1], self.team2_pyd[1])

            # Print Rush YPG
            print("Rushing Yards:")
            print(f"{self.team1} : {self.team1_ryd[0]:.1f} ({self.team1_ryd[1]})")
            print(f"{self.team2} : {self.team2_ryd[0]:.1f} ({self.team2_ryd[1]})")
            # Compare YPG
            self.ryd_diff = self.compare_stats(self.team1_ryd[0], self.team2_ryd[0], self.team1_ryd[1], self.team2_ryd[1])

            # Print Opp PPG
            print("Opponent PPG:")
            print(f"{self.team1} : {self.team1oppg[0]:.1f} ({self.team1oppg[1]})")
            print(f"{self.team2} : {self.team2oppg[0]:.1f} ({self.team2oppg[1]})")
            # Compare PPG
            self.oppg_diff = self.compare_stats(self.team1oppg[0], self.team2oppg[0], self.team1oppg[1], self.team2oppg[1], lower_is_better=True)

            # Print OYPG
            print("Opponent Yards:")
            print(f"{self.team1} : {self.team1oypg[0]:.1f} ({self.team1oypg[1]})")
            print(f"{self.team2} : {self.team2_oypg[0]:.1f} ({self.team2_oypg[1]})")
            # Compare YPG
            self.oypg_diff = self.compare_stats(self.team1oypg[0], self.team2_oypg[0], self.team1oypg[1], self.team2_oypg[1], lower_is_better=True)

            # Print Opp YPG
            print("Opponent Pass Yards: ")
            print(f"{self.team1} : {self.team1oypg[0]:.1f} ({self.team1oypg[1]})")
            print(f"{self.team2} : {self.team2_opyd[0]:.1f} ({self.team2_opyd[1]})")
            # Compare YPG
            self.oypg_diff = self.compare_stats(self.team1oypg[0], self.team2_opyd[0], self.team1oypg[1], self.team2_opyd[1], lower_is_better=True)

            # Print Opp Rush Yards
            print("Opponent Rushing Yards:")
            print(f"{self.team1} : {self.team1_oryd[0]:.1f} ({self.team1_oryd[1]})")
            print(f"{self.team2} : {self.team2_oryd[0]:.1f} ({self.team2_oryd[1]})")
            # Compare YPG
            self.oryd_diff = self.compare_stats(self.team1_oryd[0], self.team2_oryd[0], self.team1_oryd[1], self.team2_oryd[1], lower_is_better=True)

            # Print Pass Pro
            print("Pass Block Sack Rate:")
            print(f"{self.team1} : {self.team1_sacks_all[0]:.1f} ({self.team1_sacks_all[1]})")
            print(f"{self.team2} : {self.team2_sacks_all[0]:.1f} ({self.team2_sacks_all[1]})")
            # Compare YPG
            self.sacks_all_diff = self.compare_stats(self.team1_sacks_all[0], self.team2_sacks_all[0], self.team1_sacks_all[1], self.team2_sacks_all[1], lower_is_better=True)

            # Print Pass Rush
            print("Pass Rush / Sack Rate:")
            print(f"{self.team1} : {self.team1_sacks[0]:.1f} ({self.team1_sacks[1]})")
            print(f"{self.team2} : {self.team2_sacks[0]:.1f} ({self.team2_sacks[1]})")
            # Compare YPG
            self.sacks_diff = self.compare_stats(self.team1_sacks[0], self.team2_sacks[0], self.team1_sacks[1], self.team2_sacks[1])

            # Print 3rd Down
            print("3rd Down Off:")
            print(f"{self.team1} : {self.team1_third_down[0]:.1f} ({self.team1_third_down[1]})")
            print(f"{self.team2} : {self.team2_third_down[0]:.1f} ({self.team2_third_down[1]})")
            # Compare YPG
            self.third_down_diff = self.compare_stats(self.team1_third_down[0], self.team2_third_down[0], self.team1_third_down[1], self.team2_third_down[1])

            # Print Redzone Off
            print("Redzone Off:")
            print(f"{self.team1} : {self.team1_redzone[0]:.1f} ({self.team1_redzone[1]})")
            print(f"{self.team2} : {self.team2_redzone[0]:.1f} ({self.team2_redzone[1]})")
            # Compare YPG
            self.redzone_diff = self.compare_stats(self.team1_redzone[0], self.team2_redzone[0], self.team1_redzone[1], self.team2_redzone[1])


            print("_______________________________________________________\n")

from project import Project

class matchups:
    def __init__(self, team1='', team2='', team1rank='', team2rank='', team1ppg='', team2ppg='', team1sos='', team2sos='', team1oppg='', team2oppg='',team1efg='', team2efg='',
                 team1oefg='', team2oefg='', team1reb='', team2reb='', team13pp='', team23pp='',team1o3pp='', team2o3pp='', team1_perc_from_three='',
                 team2_perc_from_three='', team1pospg='', team2pospg='', team1eff_poss_ratio='', team2eff_poss_ratio='', team1opp_eff_poss_ratio='', team2opp_eff_poss_ratio='', array='',
                 team1_home_rating='', team2_home_rating='', team1_away_rating='', team2_away_rating='', team1_l5_rating='', team2_l5_rating=''):
        self.team1 = team1
        self.team2 = team2
        self.team1rank = int(team1rank)
        self.team2rank = int(team2rank)
        self.rank_diff = ''
        self.team1ppg = team1ppg
        self.team2ppg = team2ppg
        self.ppg_diff = ''
        self.team1sos = int(team1sos)
        self.team2sos = int(team2sos)
        self.sos_diff = ''
        self.team1oppg = team1oppg
        self.team2oppg = team2oppg
        self.oppg_diff = ''
        self.team1efg = team1efg
        self.team2efg = team2efg
        self.efg_diff = ''
        self.team1oefg = team1oefg
        self.team2oefg = team2oefg
        self.oefg_diff = ''
        self.team1reb = team1reb
        self.team2reb = team2reb
        self.reb_diff = ''
        self.team13pp = team13pp
        self.team23pp = team23pp
        self.threepp_diff = ''
        self.team1o3pp = team1o3pp
        self.team2o3pp = team2o3pp
        self.team1_perc_from_three = team1_perc_from_three
        self.team2_perc_from_three = team2_perc_from_three
        self.per_from_three_diff = ''
        self.o3pp_diff = ''
        self.team1pospg = team1pospg
        self.team2pospg = team2pospg
        self.pospg_diff = ''
        self.team1eff_poss_ratio = team1eff_poss_ratio
        self.team2eff_poss_ratio = team2eff_poss_ratio
        self.team1opp_eff_poss_ratio = team1opp_eff_poss_ratio
        self.team2opp_eff_poss_ratio = team2opp_eff_poss_ratio
        self.team1_home_rating = team1_home_rating
        self.team2_home_rating = team2_home_rating
        self.team1_away_rating = team1_away_rating
        self.team2_away_rating = team2_away_rating
        self.team1_l5_rating = team1_l5_rating
        self.team2_l5_rating = team2_l5_rating
        self.l5_diff = ''

        self.array = array


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

            # Print SOS
            print("Strength of Schedule:")
            print(f"{self.team1} : {self.team1sos}")
            print(f"{self.team2} : {self.team2sos}",end='')
            # Call get_diff
            self.sos_diff = self.get_diff('sos')



            # Print PPG
            print("points Per Game:")
            print(f"{self.team1} : {self.team1ppg[0]:.1f} ({self.team1ppg[1]})")
            print(f"{self.team2} : {self.team2ppg[0]:.1f} ({self.team2ppg[1]})")
            # Compare PPG
            self.ppg_diff = self.compare_stats(self.team1ppg[0], self.team2ppg[0], self.team1ppg[1], self.team2ppg[1])

            #print OPPG
            print("Opponent Points Per Game:")
            print(f"{self.team1} : {self.team1oppg[0]:.1f} ({self.team1oppg[1]})")
            print(f"{self.team2} : {self.team2oppg[0]:.1f} ({self.team2oppg[1]})")
            # Compare PPG

            self.oppg_diff = self.compare_stats(self.team1oppg[0], self.team2oppg[0], self.team1oppg[1], self.team2oppg[1], True)


            # print EFG%
            print("Effective FG%:")
            print(f"{self.team1} : {self.team1efg[0]:.1f}% ({self.team1efg[1]})")
            print(f"{self.team2} : {self.team2efg[0]:.1f}% ({self.team2efg[1]})")
            # Compare PPG
            self.efg_diff = self.compare_stats(self.team1efg[0], self.team2efg[0], self.team1efg[1], self.team2efg[1])


            # print OEFG%
            print("Opponent Effective FG%:")
            print(f"{self.team1} : {self.team1oefg[0]:.1f}% ({self.team1oefg[1]})")
            print(f"{self.team2} : {self.team2oefg[0]:.1f}% ({self.team2oefg[1]})")
            # Compare PPG
            self.oefg_diff = self.compare_stats(self.team1oefg[0], self.team2oefg[0], self.team1oefg[1], self.team2oefg[1], True)


            # print Rebound Rate
            print("Rebount Rate:")
            print(f"{self.team1} : {self.team1reb[0]:.1f}% ({self.team1reb[1]})")
            print(f"{self.team2} : {self.team2reb[0]:.1f}% ({self.team2reb[1]})")
            # Compare PPG
            self.reb_diff = self.compare_stats(self.team1reb[0], self.team2reb[0], self.team1reb[1], self.team2reb[1])

            #print 3 point %
            print("3 Point %:")
            print(f"{self.team1} : {self.team13pp[0]:.1f}% ({self.team13pp[1]})")
            print(f"{self.team2} : {self.team23pp[0]:.1f}% ({self.team23pp[1]})")
            self.threepp_diff = self.compare_stats(self.team13pp[0], self.team23pp[0], self.team13pp[1], self.team23pp[1])

            # print Opponent 3 point %
            print("Opponent 3 Point %:")
            print(f"{self.team1} : {self.team1o3pp[0]:.1f}% ({self.team1o3pp[1]})")
            print(f"{self.team2} : {self.team2o3pp[0]:.1f}% ({self.team2o3pp[1]})")
            self.o3pp_diff = self.compare_stats(self.team1o3pp[0], self.team2o3pp[0], self.team1o3pp[1],self.team2o3pp[1], True)

            # print % points from 3
            print("% of points from 3:")
            print(f"{self.team1} : {self.team1_perc_from_three[0]:.1f}% ({self.team1_perc_from_three[1]})")
            print(f"{self.team2} : {self.team2_perc_from_three[0]:.1f}% ({self.team2_perc_from_three[1]})")
            self.per_from_three_diff = self.compare_stats(self.team1_perc_from_three[0], self.team2_perc_from_three[0], self.team1_perc_from_three[1], self.team2_perc_from_three[1])

            # print Home Rating
            print("Home Rating:")
            print()
            print(f"{self.team1} : {self.team1_home_rating[0]} ({self.team1_home_rating[1]})")
            print(f"{self.team2} : {self.team2_home_rating[0]} ({self.team2_home_rating[1]})")

            # print Away Rating
            print("Away Rating:")
            print(f"{self.team1} : {self.team1_away_rating[0]} ({self.team1_away_rating[1]})")
            print(f"{self.team2} : {self.team2_away_rating[0]} ({self.team2_away_rating[1]})")

            # print Last 5 Rating
            print("Last 5 Rating:")
            print(f"{self.team1} : {self.team1_l5_rating[0]} ({self.team1_l5_rating[1]})")
            print(f"{self.team2} : {self.team2_l5_rating[0]} ({self.team2_l5_rating[1]})")
            self.l5_diff = self.compare_stats(self.team1_l5_rating[0], self.team2_l5_rating[0], self.team1_l5_rating[1], self.team2_l5_rating[1])


            print("_______________________________________________________\n")











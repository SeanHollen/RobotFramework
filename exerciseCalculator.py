from enum import Enum, auto

class M(Enum): 
    BICEPS = auto()
    TRICEPS = auto()
    DELTS = auto()
    CHEST = auto()
    ABS = auto()
    LATS = auto()
    TRAPS = auto()
    LOWER_BACK = auto()
    CALVES = auto()
    HAMSTRINGS = auto()
    QUADS = auto()
    GLUTES = auto()
    FOREARMS = auto()

class ExerciseCalculator(object):

    muscle_groups = {
        "push": [M.TRICEPS, M.CHEST, M.DELTS], 
        "pull": [M.LATS, M.TRAPS, M.LOWER_BACK, M.BICEPS], 
        "legs": [M.CALVES, M.HAMSTRINGS, M.QUADS, M.GLUTES], 
        "back": [M.LATS, M.TRAPS, M.LOWER_BACK], 
        "arms": [M.BICEPS, M.TRICEPS, M.DELTS, M.FOREARMS]
        }

    def __init__(self, min_w=8, max_w=20):
        self.min_work = min_w
        self.max_work = max_w
        self.set_counts()
        self.init_exercise_info()

    def set_counts(self): 
        self.totals_per = self.generate_exercise_dictionary()
        self.total_volumes_per = self.generate_exercise_dictionary()
    
    def generate_exercise_dictionary(self): 
        dict = {
            M.CALVES: 0, M.HAMSTRINGS: 0, M.QUADS: 0, M.GLUTES: 0,
            M.BICEPS: 0, M.TRICEPS: 0, M.DELTS: 0, M.FOREARMS: 0,
            "chest": 0, "abs": 0, M.LATS: 0, M.TRAPS: 0, M.LOWER_BACK: 0
            }
        return dict

    def init_exercise_info(self):
        squats = {M.GLUTES: 3, M.QUADS: 3, M.HAMSTRINGS: 2, M.LOWER_BACK: 2, M.CALVES: 1, "abs": 1}
        bench_press = {"chest": 3, M.TRICEPS: 3, M.DELTS: 2, M.BICEPS: 2, M.FOREARMS: 1}
        overhead_press = {M.DELTS: 3, M.TRICEPS: 3, "chest": 2, M.BICEPS: 2, M.FOREARMS: 1}
        flyes = {"chest": 3, M.DELTS: 2, M.BICEPS: 1}
        calf_raises = {M.CALVES: 3}
        rows = {M.LATS: 3, M.TRAPS: 3, M.BICEPS: 2, M.LOWER_BACK: 1}
        curls = {M.BICEPS: 3, M.DELTS: 1}
        tricep_pushdowns = {M.TRICEPS: 3, M.DELTS: 1}
        chinups = {M.BICEPS: 3, M.LATS: 3, M.TRAPS: 2, "abs": 2, M.FOREARMS: 2}
        pullups = {M.LATS: 3, M.BICEPS: 2, M.TRAPS: 2, "abs": 2, M.FOREARMS: 2}
        dips = {M.TRICEPS: 3, M.DELTS: 2, "chest": 2, M.FOREARMS: 1, M.LATS: 1}
        hanging_leg_raises = {"abs": 3, M.QUADS: 2, M.FOREARMS: 2}
        deadlifts = {M.GLUTES: 3, M.LOWER_BACK: 3, M.TRAPS: 2, M.QUADS: 2, M.CALVES: 2, 
        M.FOREARMS: 2, M.HAMSTRINGS: 1, "abs": 1}
        shrugs = {M.FOREARMS: 3, M.TRAPS: 3}
        farmers_carries = {M.FOREARMS: 3, M.TRAPS: 2}
        rack_pulls = {M.FOREARMS: 3, M.TRAPS: 2, M.GLUTES: 1, M.LOWER_BACK: 1, M.QUADS: 1}
        situps = {"abs": 3}
        tricep_pullovers = {M.TRICEPS: 3}
        leg_curls = {M.HAMSTRINGS: 3}
        leg_extensions = {M.QUADS: 3}
        face_pulls = {M.DELTS: 3, M.TRAPS: 1, M.BICEPS: 1}
        lat_raises = {M.DELTS: 3}
        leg_press = {M.GLUTES: 3, M.QUADS: 3, M.HAMSTRINGS: 2, M.CALVES: 1}
        self.exercise_info = {
            "squats": squats, "bench press": bench_press, "overhead press": overhead_press, 
            "flyes": flyes, "calf raises": calf_raises, "rows": rows, "curls": curls, 
            "tricep pushdowns": tricep_pushdowns, "chinups": chinups, "chin ups": chinups, 
            "pullups": pullups, "pull ups": pullups, "sit ups": situps,
            "dips": dips, "hanging leg raises": hanging_leg_raises, "deadlifts": deadlifts, 
            "shrugs": shrugs, "farmers carries": farmers_carries, "farmer's carries": farmers_carries, 
            "rack pulls": rack_pulls, "situps": situps, "tricep pullovers": tricep_pullovers, 
            "leg curls": leg_curls, "leg extensions": leg_extensions, "face pulls": face_pulls, 
            "lat raises": lat_raises, "leg press": leg_press
        }

    def push(self, exercise, sets, reps=8): 
        if sets <= 0: 
            raise ExerciseError("nonpositive sets")
        exercise = exercise.lower()
        if exercise in self.exercise_info:
            for key in self.exercise_info[exercise]: 
                new_sets = self.exercise_info[exercise][key] * sets
                self.totals_per[key] = self.totals_per[key] + new_sets
                new_volume = self.exercise_info[exercise][key] * sets * reps
                self.total_volumes_per[key] = self.totals_per[key] + new_volume
        else: 
            raise ExerciseError("invalid exercise: " + exercise)

    def reduce_counts_by(self, percent=1):
        if percent == 1: 
            self.set_counts()
            return
        for key in self.totals_per:
            self.totals_per[key] = self.totals_per[key] * (1 - percent)
        for key in self.total_volumes_per:
            self.total_volumes_per[key] = self.total_volumes_per[key] * (1 - percent)

    def get_undertrained(self): 
        results = []
        for key in self.totals_per: 
            if self.totals_per[key] < self.min_work:
                results.append(key)
        return results

    def get_not_undertrained(self): 
        results = []
        for key in self.totals_per: 
            if self.totals_per[key] >= self.min_work:
                results.append(key)
        return results

    def get_overtrained(self): 
        results = []
        for key in self.totals_per: 
            if self.totals_per[key] > self.max_work:
                results.append(key)
        return results

    def get_properly_trained(self): 
        results = []
        for key in self.totals_per: 
            if self.totals_per[key] > self.min_work and self.totals_per[key] < self.max_work:
                results.append(key)
        return results

    def least_trained_muscle(self): 
        least = ""
        amount = 10000
        for key in self.totals_per: 
            if self.totals_per[key] < amount:
                amount = self.totals_per[key]
                least = key
        return least + " " + amount

    def most_trained_muscle(self): 
        most = ""
        amount = -1
        for key in self.totals_per: 
            if self.totals_per[key] > amount:
                amount = self.totals_per[key]
                most = key
        return most + " " + amount

    def get_most_trained_by_volume(self): 
        most = ""
        amount = -1
        for key in self.totals_per: 
            if self.total_volumes_per[key] > amount:
                amount = self.total_volumes_per[key]
                most = key
        return most + " " + amount

    def get_least_trained_by_volume(self): 
        least = ""
        amount = 10000
        for key in self.totals_per: 
            if self.totals_per[key] < amount:
                amount = self.totals_per[key]
                least = key
        return least + " " + amount

    def get_sets_by_muscle_group(self, group): 
        if group in self.muscle_groups:
            total = 0
            for key in self.muscle_groups[group]:
                total = total + self.totals_per[key]
        else:
            raise AssertionError("muscle group not recorded: " + group)

class ExerciseError(Exception):
    pass

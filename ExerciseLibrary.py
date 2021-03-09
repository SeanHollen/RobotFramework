from exerciseCalculator import ExerciseCalculator, ExerciseError

class ExerciseLibrary(object):
    #Test library for testing fitness routine business logic.

    def __init__(self):
        self._exercises = ExerciseCalculator()

    def exercise(self, exercise):
        """
        Example:
        or
            Exercise    bench press: 4 sets
        or
            Exercise    bench press: 4 sets 5 reps
        """
        split = exercise.split(":")
        ex = split[0].strip()
        sets_and_reps = split[1].strip().split(" ")
        sets = int(sets_and_reps[0].strip())
        if len(sets_and_reps) == 4: 
            reps = int(sets_and_reps[2].strip())
            self._exercises.push(ex, sets, reps)
        else: 
            self._exercises.push(ex, sets)

    def rest(self, amount): 
        self._exercises.reduce_counts_by(float(amount))

    def full_rest(self): 
        self._exercises.set_counts()

    def summary(self): 
        result = ""
        result = result + str(len(self._exercises.get_undertrained())) + " "
        result = result + str(len(self._exercises.get_properly_trained())) + " " 
        result = result + str(len(self._exercises.get_overtrained()))
        return result

    def expect_summary(self, summary): 
        actual = self.summary()
        if actual != summary:
            raise AssertionError('%s != %s' % (actual, summary))

    def expect_least_trained(self, result):
        actual = self._exercises.least_trained_muscle()
        if actual != result:
            raise AssertionError('%s != %s' % (actual, result))

    def expect_most_trained(self, result):
        actual = self._exercises.most_trained_muscle()
        if actual != result:
            raise AssertionError('%s != %s' % (actual, result))

    #do
    def expect_no_undertrained(self): 
        actual = len(self._exercises.get_undertrained())
        if actual != 0:
            raise AssertionError("There were " + str(actual) + " undertrained")

    #do
    def expect_no_overtrained(self): 
        actual = len(self._exercises.get_overtrained())
        if actual != 0:
            raise AssertionError("There were " + str(actual) + " overtrained")

    #do
    def should_cause_error(self, exercise):
        try:
            self.exercise(exercise)
        except ExerciseError as err:
            return str(err)
        else:
            raise AssertionError(
        "'%s' should have caused an error." % exercise)


import time


def retry(
    function,
    attempts=3
):


    for i in range(attempts):

        try:

            return function()


        except Exception as e:


            print(
                f"Attempt {i+1} failed:",
                e
            )


            if i == attempts-1:

                raise e


            time.sleep(2)
# Random Participant Picker

- This is a script that will be used to pick a random user among those that checked-in to a
  specified ACM event through Portal.

## How to use this script:

1. Install `firebase_admin` by running the following command:

   ```
   $ pip install firebase_admin
   ```

2. Go to Firebase console to generate a JSON file containing your project's private key.

3. Specify the id of the event of interest along with the filename of the private key JSON file in the global variables on top of the `main.py` file

4. Execute the script with the following command and it will produce basic information of the lucky participant.
   ```
   $ python -u main.py
   ```

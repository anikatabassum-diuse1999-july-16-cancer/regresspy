

Regresspy is a python module for carrying out simple regressions using gradient descent algorithm. However, the library is half complete. My  task is to fill in the necessary codes. The tasks of the project is done  below:

 I have Fork this repository.Then I have  Create a new branch using my username.**I have Committed frequently, usually everytime after changing or completing a function I have made  the commit messages clear and complete.** . I have written  the codes for the mean absolute, sum of squared, mean squared, and root mean squared errors in the 'loss.py' file. I have Complete the test_loss.py by filling in the codes to test above functions. An example for testing mae is already given. 
After that, I have gone  to thgradient_decent.py file. It contains two functions named 'forward' for computing forward propagation and 'backward' for computing the gradients. The second one is already done for me. All you have done is fill in the codes for forward propagation.
 Then I  went to the main.py file where the actual training will take place. The first task is to complete the '_initialize_weight_ function. Then complete the ' _train'  function. Finally, complete the 'predicx and `score` function. Now, go the 'model.py' file in the `test` folder. Here, you will perform two regressions. First one will be carried out using the `SGDRegressor` from the `sklearn` library. Second one will be carried out using your own codes. Compare the results and write in the `README.md` file (You can delete this README file).
Next I  Fill in the `requirements.txt` file according to the libraries you have used in your codes. I have Fill-in the `setup.py` file to install your code as a library.e 
 Here the RMSE value is 0.543215 . The epoch is 40 and learning rate is 0.001 . Final RMSE value is 0.157635. 

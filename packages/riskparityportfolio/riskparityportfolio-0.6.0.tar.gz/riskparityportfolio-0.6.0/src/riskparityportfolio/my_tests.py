import numpy as np
import matplotlib.pyplot as plt
import riskparityportfolio as rpp


def main():
    N = 100
    b = np.ones(N) / N
    np.random.seed(42)
    U = np.random.multivariate_normal(mean=np.zeros(N), cov=0.1 * np.eye(N), size=round(.7 * N)).T
    Sigma = U @ U.T  # singular covariance matrix

    my_portfolio = rpp.RiskParityPortfolio(Sigma, budget=b)
    my_portfolio.design(verbose=False, tau=1e-10)  # <-- force ill-conditioned matrix
    w_ref = my_portfolio.weights



def main2():
    N = 100
    b = np.ones(N)/N
    np.random.seed(42)
    U = np.random.multivariate_normal(mean=np.zeros(N), cov=0.1 * np.eye(N), size=round(.7 * N)).T
    Sigma = U @ U.T + np.eye(N)
    my_portfolio = rpp.RiskParityPortfolio(Sigma, budget=b)
    my_portfolio.design()
    w = my_portfolio.weights

    objective_function_vector = np.array(my_portfolio.sca.objective_function)
    plt.figure()
    plt.plot(objective_function_vector)
    plt.title('Objective Function Values')
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.show()




def other():
    N = 50
    np.random.seed(42)
    U = np.random.multivariate_normal(mean=np.zeros(N), cov=0.1 * np.eye(N), size=round(.7 * N)).T
    Sigma = U @ U.T + np.eye(N)

    # Bounds for sum: 0.5 <= sum(w) <= 1 (tending to upper bound)
    my_portfolio = rpp.RiskParityPortfolio(Sigma)
    my_portfolio.add_mean_return(alpha=1e-8, mean=np.ones(N))  # this adds the sum(w) to also maximize sum(w)
    my_portfolio.design(Cmat=np.empty((0, N)), cvec=[],
                        Dmat=np.vstack([-np.ones((1,N)), np.ones((1,N))]), dvec=np.array([-0.5, 1]))
    w = my_portfolio.weights
    np.testing.assert_almost_equal(np.sum(w), 1.0)

    # Bounds for sum: 0.5 <= sum(w) <= 1 (tending to lower bound)
    my_portfolio = rpp.RiskParityPortfolio(Sigma)
    my_portfolio.add_mean_return(alpha=1e-8, mean=-np.ones(N))  # this adds the sum(w) to also maximize sum(w)
    my_portfolio.design(Cmat=np.empty((0, N)), cvec=[],
                        Dmat=np.vstack([-np.ones((1,N)), np.ones((1,N))]), dvec=np.array([-0.5, 1]))
    w = my_portfolio.weights
    np.testing.assert_almost_equal(np.sum(w), 0.5)

    # objective_function_vector = np.array(my_portfolio.sca.objective_function)
    # plt.figure()
    # plt.plot(objective_function_vector)
    # plt.title('Objective Function Values')
    # plt.xlabel('Iteration')
    # plt.ylabel('Value')
    # plt.show()


if __name__ == "__main__":
    main()
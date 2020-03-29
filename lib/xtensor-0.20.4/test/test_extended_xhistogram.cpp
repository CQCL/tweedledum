/***************************************************************************
* Copyright (c) 2016, Johan Mabille, Sylvain Corlay and Wolf Vollprecht    *
*                                                                          *
* Distributed under the terms of the BSD 3-Clause License.                 *
*                                                                          *
* The full license is in the file LICENSE, distributed with this software. *
****************************************************************************/

// This file is generated from test/files/cppy_source/test_extended_xhistogram.cppy by preprocess.py!

#include <algorithm>

#include "gtest/gtest.h"
#include "xtensor/xarray.hpp"
#include "xtensor/xtensor.hpp"
#include "xtensor/xhistogram.hpp"

namespace xt
{
    using namespace xt::placeholders;

    /*py

    a = (np.random.random(1000) * 51).astype(np.int)

    count, bin_edges  = np.histogram(a, 50)

    prob, _  = np.histogram(a, 50, density=True)

    */
    TEST(xtest_extended_histogram, histogram_auto)
    {
        // py_a
        xarray<long> py_a = {19,48,37,30, 7, 7, 2,44,30,36, 1,49,42,10, 9, 9,15,26,22,14,31, 7,14,18,
                             23,40,10,26,30, 2,30, 8, 3,48,49,41,15, 4,34,22, 6,25, 1,46,13,33,15,26,
                             27, 9,49,39,47,45,30,47, 4, 9, 2,16,19,13,42,18,14,27, 7,40, 3,50,39,10,
                              0,41,36,37,39, 3,18, 5,44,31,16, 3,15,16,37,32,45,24, 6,36,38,28,39,25,
                             26,21, 1, 5, 1,32,16,25,46,12,20,38,11, 3,14, 8,47,41,32,44,40, 9,45,27,
                             41,45,16, 5,11,21,41,43, 0,26,21,11, 6,17,48,16,26,35,18,49,49,12,25,15,
                             14, 1,31,25, 2,14,46,12, 7,24,50,12,34,38,12,37,18,32,32,27, 4,42,16, 9,
                              2,30,34, 0,26,11,32, 8,35,19,47, 7,17, 5,47,44,13,33,41,28,27,12, 4,45,
                             45,32,17,17,37,45,45,39,32, 4, 8,45,30, 0, 5,33, 0, 8,27,35,33,11,36,12,
                             16,38,33,43,33,28, 4,18,13,12,49,20,45,32,40,25,29,25, 9,36,14, 1,32, 9,
                             47,48,46,18, 0,47,21,49,49,43,15,19,43,16, 8,28,47,35,29, 4,31,50, 7,26,
                             44,37,35,35,18,14,41,41,44,46,26,25,40,33,35,40,45,17,19, 4,29, 1,23,27,
                             14,30, 1, 1,41,18, 6,26,39,11,31, 4, 2,27,27,32,37,49,26,16,40,13,22, 4,
                              1,49,42,35,20, 8, 7,12,28,36,33,14,48,37,28,31,21,12,18,38, 0, 5, 2, 2,
                             43,35,24, 4,25,24, 8,22,20,31,32, 2,19,31,25,43,33, 8, 3,32, 1,29,47,29,
                             19,32,23,27,48,19,49,46, 9, 3, 5, 0, 4,34, 3,16,43, 1,41,14, 6,35,32,44,
                             37,40,14, 9,38,41,50,21,18,39,17,47,43,21,38,38, 5,46,25,42,16,45,19, 0,
                             46, 4,16,48,48,29,32,22,14,16,34,38,40,40, 4,25, 2,28,22,45,17, 5, 7,38,
                             31, 5, 4,35, 3,41,36, 4, 4,50,19,18,41,48,50,38,19, 4,39,28,21,46, 5,25,
                              0,23, 2, 6, 5,33,38,29,49,19,14,44,11,49, 0,49, 2,45,26,50, 3,28,49,26,
                             32,35,23,32,29,45, 2,14,48,45,23,31,14, 9,23,18,29, 3,49,50,35,27,15,41,
                             34, 8,46,41,48,37,31,21,47,44, 2, 1,19,41,50, 7,30,19,49,42,42,23,21,13,
                              2,44,41,50,50,28,39,48,43,12,22, 6,48,30,11,34,31,18, 5,34,26,39,26,43,
                             28,28,44,20, 6, 1,38,31,35,10, 6, 0,17,30,20,22,46,17,26,39,20,31,43,48,
                              7,47,25,13,23,49,25,16,32,12, 3, 6, 6, 7, 7,32, 9,17,45,24,34, 8, 9, 2,
                              8,14, 9, 4, 6,23,10,18,25,35, 2,40,32, 4,44,46, 3,14,41,38, 9,10,18,24,
                             31,18,23,38, 1,12,36,45,26,27, 5,22,27,12,13,19, 1,16,10,16, 6,45,30,34,
                             40,25, 4,27,29,38,22, 6,14,18,32,29,18,50,30,12, 5, 7,12, 8, 9,14, 8,45,
                              4,26,20,50, 5,20,49,44,41,13, 8,34,47,28,29,14,39, 9,16,21,25,12, 5,31,
                             14,29, 7,24,27, 2,17, 6, 3,50,16,41,12,34,38,30,24,21,17,47,42,49, 6,37,
                             47, 9, 3,37,29,42, 7,40,10, 8, 8,41,33,26,18,44,20,41,22,19,23,15,38,25,
                             11,45,19,27,46,31, 5,47,32,17, 7,40,31,27,45,40, 7,15,12,37, 1,29,38,44,
                             17,41, 5,43, 6,20,40, 7,11,36,36,32,35,27,12,17, 9,46,29,20,23,48, 7,29,
                             25,31, 0,44,47,28,35,47,36, 7,29,30,21,37,47,47,22, 5,50,42, 6,46,44,26,
                             30,20, 2,17,40, 0,17,20,27,46,17,17,37,23,11,23, 7, 8,25,21,46,18,29,32,
                              0,33, 9,49, 7,21, 4,50,25,30, 3,38,10,45,10, 9, 1,24,28, 3,39,23,26,22,
                             20,28, 7, 9,43,48,19,13,32,20, 1, 7,36,33, 1,11,11,34, 1, 5,40, 9,33,12,
                              5,12,36,43,42,20,34,10,14,45, 0, 4,10, 1, 9,29,21,45,41,17,13,19,30,13,
                             31,20,28,22,15,48,38, 7,44,24,45,40,21, 1,13,27,32,13, 7,42,50,26, 8,13,
                              0,46, 6,29,13,28,33,42,10, 0, 6,45,44,30,30,33, 8,46,21,19,26, 2, 8,37,
                              4,30,12,19,14,18,36,15,28,24,33,47,37,10, 1,13,30, 2,25,30,17,39, 5, 3,
                             37,25,35,22,12,41,40,35,13,30,18, 4,46, 6,48,22};
        // py_bin_edges
        xarray<double> py_bin_edges = { 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.,10.,11.,12.,13.,14.,15.,16.,17.,
                                       18.,19.,20.,21.,22.,23.,24.,25.,26.,27.,28.,29.,30.,31.,32.,33.,34.,35.,
                                       36.,37.,38.,39.,40.,41.,42.,43.,44.,45.,46.,47.,48.,49.,50.};
        // py_count
        xarray<long> py_count = {18,24,21,18,26,23,21,27,21,24,14,13,24,18,24,11,19,21,23,21,18,18,16,16,
                                 11,24,23,20,19,21,24,20,27,17,14,19,14,18,21,14,20,25,13,14,19,27,20,21,
                                 18,38};
        // py_prob
        xarray<double> py_prob = {0.018,0.024,0.021,0.018,0.026,0.023,0.021,0.027,0.021,0.024,0.014,0.013,
                                  0.024,0.018,0.024,0.011,0.019,0.021,0.023,0.021,0.018,0.018,0.016,0.016,
                                  0.011,0.024,0.023,0.02 ,0.019,0.021,0.024,0.02 ,0.027,0.017,0.014,0.019,
                                  0.014,0.018,0.021,0.014,0.02 ,0.025,0.013,0.014,0.019,0.027,0.02 ,0.021,
                                  0.018,0.038};

        auto bin_edges = xt::histogram_bin_edges(py_a, std::size_t(50));

        auto count = xt::histogram(py_a, bin_edges);

        auto prob = xt::histogram(py_a, bin_edges, true);

        EXPECT_EQ(xt::cast<double>(bin_edges), py_bin_edges);

        EXPECT_EQ(count, xt::cast<double>(py_count));

        EXPECT_EQ(prob, py_prob);
    }
}

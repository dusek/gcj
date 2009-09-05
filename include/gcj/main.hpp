#ifndef GCJ_MAIN_HPP_
#define GCJ_MAIN_HPP_

#include <memory>
#include <iostream>
#include <fstream>
#include <cassert>
#include <gcj/Solver.h>
#ifdef GCJ_PARALLELIZE
#include <tbb/pipeline.h>
#endif
#include <functional>
#ifdef GCJ_PROGRESS_BAR
#include <boost/progress.hpp>
#endif

#include <istream>
#include <ostream>

namespace {
#ifdef GCJ_PARALLELIZE
    // Parallel stuff
    class case_filter: public tbb::filter {
    protected:
        case_filter(tbb::filter::mode mode)
            :
        tbb::filter(mode)
        {}

    public:
        virtual void *operator()(void *item) {
            process_case(static_cast<gcj::Case *>(item));
            return item;
        }

        virtual void finalize(void *item) {
            gcj::Case *case_ = static_cast<gcj::Case *>(item);
            delete case_;
        }

    protected:
        virtual void process_case(gcj::Case *case_) = 0;

    };

    class tbb_input_filter : public tbb::filter {
        std::istream& m_input;
        gcj::Solver& m_solver;
        std::size_t m_cases_left;
    public:
        tbb_input_filter(std::istream& i, gcj::Solver& solver, std::size_t case_count)
            :
        tbb::filter(tbb::filter::serial_in_order),
        m_input(i),
        m_solver(solver),
        m_cases_left(case_count)
        {}

        virtual void *operator()(void *item) {
            if (m_cases_left-- > 0)
                return m_solver.parse_one_case(m_input);
            else
                return 0;
        }
    };

    class tbb_solving_filter : public case_filter {
    public:
        tbb_solving_filter()
            :
        case_filter(tbb::filter::parallel)
        {}

        virtual void process_case(gcj::Case *case_) {
            case_->solve();
        }
    };

    class tbb_output_filter : public case_filter {
        std::ostream& m_output;
        std::size_t m_case_idx;
        std::size_t m_case_count;
#ifdef GCJ_PROGRESS_BAR
        boost::progress_display m_progress_display;
#endif
    public:
        tbb_output_filter(std::ostream& o, std::size_t case_count)
            :
        case_filter(tbb::filter::serial_in_order),
        m_output(o),
        m_case_idx(0),
        m_case_count(case_count)
#ifdef GCJ_PROGRESS_BAR
        ,
        m_progress_display(m_case_count, std::cerr)
#endif
        {}

        virtual void process_case(gcj::Case *case_) {
#ifdef GCJ_PROGRESS_BAR
            ++m_progress_display;
#else
            std::clog << "Solved case " << m_case_idx + 1 << std::endl;
#endif
            case_->output_solution(m_output, m_case_idx++);
        }
    };

    class tbb_delete_filter : public case_filter {
    public:
        tbb_delete_filter()
            :
        case_filter(tbb::filter::parallel)
        {}

        virtual void process_case(gcj::Case *case_) {
            delete case_;
        }
    };
#endif
}

namespace gcj {
    void solve(Solver& solver, std::istream &input, std::ostream& output) {
        const std::size_t case_count = solver.parse_header(input);
        const bool parallelize = 
#ifdef GCJ_PARALLELIZE
            solver.parallelize()
#else
            false
#endif
            ;

        if (parallelize) {
#ifdef GCJ_PARALLELIZE
            tbb::pipeline pipeline;
            tbb_input_filter input_filter(input, solver, case_count);
            tbb_solving_filter solving_filter;
            tbb_output_filter output_filter(output, case_count);
            tbb_delete_filter delete_filter;
            pipeline.add_filter(input_filter);
            pipeline.add_filter(solving_filter);
            pipeline.add_filter(output_filter);
            pipeline.add_filter(delete_filter);
            pipeline.run(0x7fffffff); // read: very big
#else
            assert(!"Programming error: parallelizing when parallelizing impossible");
#endif
        } else {
#ifdef GCJ_PROGRESS_BAR
            boost::progress_display progress_display(case_count, std::cerr);
#endif
            for(std::size_t case_idx = 0; case_idx < case_count; ++case_idx) {
#ifdef GCJ_PROGRESS_BAR
                ++progress_display;
#else
                std::clog << "Solving case " << case_idx + 1 << std::endl;
#endif
                const std::auto_ptr<gcj::Case> case_(solver.parse_one_case(input));
                case_->solve();
                case_->output_solution(output, case_idx);
            }
        }
    }

    int main(int argc, char **argv, Solver& solver) {
        int ret = EXIT_FAILURE;
        try {
            if ((argc < 1) || (argc > 3)) {
                throw "Usage: gcj(.exe) [<input file> [<output file>]]";
            }

            std::auto_ptr<std::istream> input_file;
            if (argc > 1) {
                input_file.reset(new std::ifstream(argv[1]));
                if (input_file->fail()) {
                    throw "Could not open input file";
                }
            }

            std::auto_ptr<std::ostream> output_file;
            if (argc > 2) {
                output_file.reset(new std::ofstream(argv[2], std::ios_base::out | std::ios_base::trunc));
                if (output_file->fail()) {
                    throw "Could not open output file";
                }
            }

            std::istream&  input = (argc > 1) ?  *input_file : std::cin ;
            std::ostream& output = (argc > 2) ? *output_file : std::cout;

            solve(solver, input, output);
            ret = EXIT_SUCCESS;

        } catch(const char *errmsg) {
            std::cerr << "Following error occured: " << errmsg   << std::endl;
        } catch(const std::exception& e) {
            std::cerr << "Following error occured: " << e.what() << std::endl;
        }
        return ret;
    }
}

#endif


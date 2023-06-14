import asyncio
import os
import random
import uvloop
import io
import time
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


X = 30
Y = 30


def generate_2d_array(n):
    array = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(n)]
    return array


async def run_testmain(par_file, index):
    # Generate TSP file
    tsp_file = '../File/prFile/tspFile/tsp_file{}.tsp'.format(index)
 
    batches = generate_2d_array(X)
    generate_tsp_file(tsp_file, batches)

    # Generate parameter file
    generate_parameter_file(par_file, index)

    # Run LKH
    cmd = ['./LKH', par_file]
    proc = await asyncio.create_subprocess_exec(*cmd)
    await proc.wait()
'''
def generate_tsp_file(filename, batches):
    with open(filename, 'w') as f:
        # Write the header
        f.write('NAME: {}\n'.format(filename))
        f.write('COMMENT: {}\n'.format('TSP file generated by Python'))
        f.write('TYPE: TSP\n')
        f.write('DIMENSION: {}\n'.format(len(batches)))
        f.write('EDGE_WEIGHT_TYPE: EUC_2D\n')
        # Write the city coordinates
        f.write('NODE_COORD_SECTION\n')
        for i, city in enumerate(batches):
            f.write('{} {} {}\n'.format(i + 1, city[0], city[1]))

        # Write the footer
        f.write('EOF\n')
'''
# 用内存读写代替磁盘读写
def generate_tsp_file(filename, batches):
    with io.StringIO() as f:
        # Write the header
        f.write('NAME: {}\n'.format(filename))
        f.write('COMMENT: {}\n'.format('TSP file generated by Python'))
        f.write('TYPE: TSP\n')
        f.write('DIMENSION: {}\n'.format(len(batches)))
        f.write('EDGE_WEIGHT_TYPE: EUC_2D\n')
        # Write the city coordinates
        f.write('NODE_COORD_SECTION\n')
        for i, city in enumerate(batches):
            f.write('{} {} {}\n'.format(i + 1, city[0], city[1]))

        # Write the footer
        f.write('EOF\n')
        # Write the memory buffer to a file
        with open(filename, 'w') as f_out:
            f_out.write(f.getvalue())


'''
def generate_parameter_file(output_filename, index):
    parameters = [
        "PROBLEM_FILE = ../File/prFile/tspFile/tsp_file{}.tsp".format(index),
        "MOVE_TYPE = 5",
        "PATCHING_C = 3",
        "PATCHING_A = 2",
        "RUNS = 10",
        "TOUR_FILE = ../File/outputFile/tourFile/lkh_output{}.txt".format(index)
    ]
    with open(output_filename, 'w') as f:
        f.write('\n'.join(parameters))
'''

# 用内存读写代替磁盘读写
def generate_parameter_file(output_filename, index):
    parameters = [
        "PROBLEM_FILE = ../File/prFile/tspFile/tsp_file{}.tsp".format(index),
        "MOVE_TYPE = 5",
        "PATCHING_C = 3",
        "PATCHING_A = 2",
        "RUNS = 5",
        "TOUR_FILE = ../File/outputFile/tourFile/lkh_output{}.txt".format(index)
    ]
    with io.open(output_filename, 'w', newline='\n') as file:
        file.write('\n'.join(parameters))

async def main():
    # Run multiple testmain functions asynchronously
    tasks = []
    # tasks：异步任务列表，由于routing的时候，每两个集单之间的状态是不会相互影响的；
    # 所以可以采用异步的方法来加速计算；
    # 异步数量设置为50,default值，但取决于公司服务器的负载;
    # range 后续应该设置为 min(50, len(batch_pool))
    semaphore = asyncio.Semaphore(Y)
    for i in range(Y):
        par_file = '../File/prFile/prFile/pr{}.par'.format(i)
        tasks.append(asyncio.create_task(run_testmain(par_file, i)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()  # 记录程序开始时间
    asyncio.run(main())
    end_time = time.time()  # 记录程序结束时间
    elapsed_time = end_time - start_time
    print("LKH执行{}个包含{}个sku的异步路径规划任务耗费的时间为：{}秒".format(Y, X, elapsed_time))
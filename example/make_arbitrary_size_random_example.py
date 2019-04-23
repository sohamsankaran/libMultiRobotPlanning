import yaml
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--num_rows', default=10, type=int)
parser.add_argument('--num_cols', default=10, type=int)
parser.add_argument('--num_agents', default=5, type=int)
parser.add_argument('--num_obstacles', default=5, type=int)
args = parser.parse_args()

instance_dict = {}

instance_dict['map'] = {}
instance_dict['map']['dimensions'] = (args.num_rows, args.num_cols)
instance_dict['agents'] = []

start_dests = {}
end_dests = {}

def make_unique_point(point_map, point_map2 = None):
    while(True):
        curr_point = (random.randint(0, args.num_rows-1), random.randint(0, args.num_cols-1))
        if(curr_point not in point_map and (point_map2 is None or curr_point not in point_map2)):
            return curr_point

for agent_num in xrange(args.num_agents):
    new_agent = {}
    new_agent['name'] = 'agent' + str(agent_num)

    # ensure that start and end points are unique
    start_point = make_unique_point(start_dests)
    start_dests[start_point] = True
    new_agent['start'] = start_point
    end_point = make_unique_point(end_dests)
    end_dests[end_point] = True
    new_agent['goal'] = end_point

    # add this agent to the instance_dict
    instance_dict['agents'].append(new_agent)

if(args.num_obstacles > 0):
    instance_dict['map']['obstacles'] = []

for obstacle_num in xrange(args.num_obstacles):
    instance_dict['map']['obstacles'].append(make_unique_point(start_dests, end_dests))

with open('../benchmark/soham_benchmarks/random_instance_dim_'+str(args.num_rows)+'_'+str(args.num_cols)+'_with_'+str(args.num_agents)+'_agents_and_'+str(args.num_obstacles)+'_obstacles.yaml', 'w') as outfile:
    yaml.dump(instance_dict, outfile, default_flow_style=False)

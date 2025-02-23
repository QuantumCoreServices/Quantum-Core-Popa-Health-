import React from 'react';
import { motion } from 'framer-motion';

const Dashboard = () => {
  return (
    <motion.div
      className="dashboard p-4"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h1 className="text-2xl font-bold mb-4">Patient Dashboard</h1>
      <p className="text-gray-700">
        Welcome to your personalized health dashboard! Here you can view your
        health stats, upcoming appointments, and more.
      </p>
    </motion.div>
  );
};

export default Dashboard;

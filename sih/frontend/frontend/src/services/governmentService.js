import api from "./governmentApi";

// Dashboard
export const getDashboardSummary = () =>
  api.get("/dashboard-summary");

export const getTopStudentSkills = () =>
  api.get("/top-student-skills");

export const getTopDemandSkills = () =>
  api.get("/top-demand-skills");

// Analytics
export const getHighestSkilledSectors = () =>
  api.get("/analytics/highest-skilled-sectors");

export const getRegionalDistribution = () =>
  api.get("/analytics/regional-distribution");

export const getSkillGap = () =>
  api.get("/analytics/skill-gap");

export const getLowestSkilledSectors = () =>
  api.get("/analytics/lowest-skilled-sectors");

// Students
export const getStudents = () =>
  api.get("/students/");

// Recruiters
export const getRecruiters = () =>
  api.get("/recruiters/");

// Jobs
export const getGovernmentJobs = () =>
  api.get("/jobs/");
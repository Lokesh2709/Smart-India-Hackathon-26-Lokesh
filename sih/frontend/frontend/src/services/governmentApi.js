import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/government",
  headers: {
    "Content-Type": "application/json",
  },
});

// ================= DASHBOARD =================

export const getDashboardSummary = () =>
  api.get("/dashboard-summary");

export const getTopStudentSkills = () =>
  api.get("/top-student-skills");

export const getTopDemandSkills = () =>
  api.get("/top-demand-skills");

export const getHighestSkilledSectors = () =>
  api.get("/highest-skilled-sectors");

export const getLowestPursuedSectors = () =>
  api.get("/lowest-pursued-sectors");

export const getRegionalDistribution = () =>
  api.get("/regional-distribution");

export const getSkillGap = () =>
  api.get("/skill-gap");

// ================= STUDENTS =================

export const getStudents = () =>
  api.get("/students/");

export const getStudentById = (id) =>
  api.get(`/students/${id}`);

export const getStudentProjects = (id) =>
  api.get(`/students/${id}/projects`);

export const getStudentProof = (id) =>
  api.get(`/students/${id}/proof`);

export const searchStudents = (params) =>
  api.get("/students/search", { params });

// ================= RECRUITERS =================

export const getRecruiters = () =>
  api.get("/recruiters/");

export const getRecruiterById = (id) =>
  api.get(`/recruiters/${id}`);

export const getIndustryDemand = () =>
  api.get("/recruiters/industry-demand");

export const getCompanyDemand = () =>
  api.get("/recruiters/company-demand");

export const getRecruiterTopSkills = () =>
  api.get("/recruiters/top-skills");

export const getChallenges = () =>
  api.get("/recruiters/challenges");

// ================= JOBS =================

export const getJobs = () =>
  api.get("/jobs/");

export const getActiveJobs = () =>
  api.get("/jobs/active");

export const getJobById = (id) =>
  api.get(`/jobs/${id}`);

export const getJobMatches = (id) =>
  api.get(`/jobs/${id}/matches`);

export const createJob = (data) =>
  api.post("/jobs/", data);

// ================= ANALYTICS =================

export const getAnalyticsSkillGap = () =>
  api.get("/analytics/skill-gap");

export const getAnalyticsRegionalDistribution = () =>
  api.get("/analytics/regional-distribution");

export const getAnalyticsHighestSkilledSectors = () =>
  api.get("/analytics/highest-skilled-sectors");

export const getAnalyticsLowestSkilledSectors = () =>
  api.get("/analytics/lowest-skilled-sectors");

export const getAnalyticsReports = () =>
  api.get("/analytics/reports");

export const getAnalyticsCampaigns = () =>
  api.get("/analytics/campaigns");

export const createCampaign = (data) =>
  api.post("/analytics/campaigns", data);

export default api;